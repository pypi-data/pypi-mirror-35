"""


"""

from __future__ import print_function
import numpy as np
import glob,litus
import datetime
from future.utils import iteritems as _iteritems


class GlobalClock(object):
    def __init__(self, t_zero = 0.0, t=0.0, dt=0.001):
        self.t = t
        self.t_zero = t_zero
        self.dt = dt
    def offset(self,d):
        return lambda: self.t + d


class InrImageStreamer(object):
    """ Reads a large inr file and is an iterator over all images.

        By default, the z dimension is ignored. Setting `z` to True changes this, such that each image is 3d instead of 2d.
    """
    def __init__(self,filename,z=False, slice_at = None):
        self.filename = filename
        self.file = open(filename,'r')
        self.raw_header = self.file.read(256)
        self.header = dict([h.split('=') for h in self.raw_header.split('\n') if '=' in h])
        self.header = dict([(k,litus._make_an_int_if_possible(v)) for k,v in _iteritems(self.header)])
        self.z = z
        self.last_image = np.zeros((50,50))
        self.start_at = 0
        self.stop_at = None
        self.step_at = None
        if slice_at is not None:
            self.start_at = slice_at.start
            self.stop_at = slice_at.stop
            self.step_at = slice_at.step
        if self.start_at is None:
            self.start_at = 0
        if self.step_at is None:
            self.step_at = 1
        self.image_i = self.start_at
    @property
    def shape(self):
        return (self.header['VDIM'],self.header['XDIM'],self.header['YDIM'])
    def reset(self):
        self.image_i = self.start_at
    def skip(self,i=1):
        self.image_i += i
        self.file.skip(self.header['ZDIM']*self.header['XDIM']*self.header['YDIM']*8)
    def seek(self,i):
        self.image_i = i
        if i >= self.header['VDIM']:
            raise StopIteration()
        self.file.seek(256 + i * self.header['ZDIM']*self.header['XDIM']*self.header['YDIM']*8)
    def read(self,i):
        self.seek(i)
        if self.header['TYPE'] == 'float' and self.header['PIXSIZE'] == '64 bits':
            if self.z:
                self.last_image = np.array([[np.frombuffer(self.file.read(self.header['ZDIM']*8),'float') for y in range(self.header['YDIM'])] for x in range(self.header['XDIM'])])
            else:
                self.last_image = np.array([np.concatenate([np.frombuffer(self.file.read(self.header['ZDIM']*8),'float') for y in range(self.header['YDIM'])],0) for x in range(self.header['XDIM'])])
            return self.last_image
        else:
            raise Exception("Not Implemented. So far only 8 byte floats are supported")
    def get_image(self):
        return self.last_image
    def _read_one_image(self):
        self.image_i += 1
        if self.header['TYPE'] == 'float' and self.header['PIXSIZE'] == '64 bits':
            a = np.array([[np.frombuffer(self.file.read(self.header['ZDIM']*8),'float') for y in range(self.header['YDIM'])] for x in range(self.header['XDIM'])])
            return a[:,:,0]
        else:
            raise Exception("Not Implemented. So far only 8 byte floats are supported")
    def get(self,i=1):
        return np.array([self._read_one_image() for ii in range(i)])
    def __iter__(self):
        def f():
            image_i = self.start_at
            max_image = self.header['VDIM']
            if self.stop_at is not None:
                max_image = self.stop_at
            while image_i < max_image:
                yield self.read(image_i)
                image_i += self.step_at
            raise StopIteration()
        return f()
    def __getitem__(self,indx):
        if type(indx) is int:
            return self.read(indx)
        if type(indx) is slice:
            return ImageStreamer(self.filename,z=self.z, slice_at=indx)
    def __len__(self):
        image_i = self.start_at
        max_image = self.header['VDIM']
        if self.stop_at is not None:
            max_image = self.stop_at
        return max_image - image_i
    def __enter__(self):
        return self
    def __exit__(self,*args):
        self.file.close()
    @property
    def buffered(self):
        return 0

class InrImageStreamWriter(object):
    def __init__(self,filename,v=1,x=1,y=1,z=1,time_dimension='VDIM'):
        """
            Usage::

                s = convis.streams.InrImageStreamWriter('stim.inr',x=inp.shape[1],y=inp.shape[2],time_dimension='ZDIM')
                with s:
                    for i in inp:
                        s.put(i[None,:,:])
        """
        self.filename = filename
        self.file = open(filename,'w')
        self.image_i = 0
        self.header = {'CPU': 'decm',
                         'PIXSIZE': '64 bits',
                         'TYPE': 'float',
                         'VDIM': v,
                         'XDIM': x,
                         'YDIM': y,
                         'ZDIM': z}
        self.last_image = np.zeros((50,50))
        self.time_dimension = time_dimension
        #self.write_header()
    def write_header(self):
        self.file.seek(0)
        self.header[self.time_dimension] = self.image_i
        header = "#INRIMAGE-4#{\n"+"\n".join([str(k) +'='+str(v) for k,v in _iteritems(self.header)])
        header = header + ('\n' * (252 - len(header))) + "##}"
        self.file.write(header)
    def __enter__(self):
        return self
    def __exit__(self,*args):
        self.write_header()
        self.file.close()
    def seek(self,i):
        self.file.seek(255 + i * self.header['ZDIM']*self.header['XDIM']*self.header['YDIM']*8)
    def get_image(self):
        return self.last_image
    def put(self,seq):
        for s in seq:
            self.write(s)
            self.last_image = s
    def write(self,img):
        if self.header['TYPE'] == 'float' and self.header['PIXSIZE'] == '64 bits':
            buff = np.array(img,dtype='float64').tobytes()
            if len(buff) == self.header['ZDIM']*self.header['XDIM']*self.header['YDIM']*8:
                self.seek(self.image_i)
                self.file.write(buff)
                self.image_i += 1
            else:
                raise Exception("Image has incorrect size:"+str(len(buff))+" != "+str(self.header['ZDIM']*self.header['XDIM']*self.header['YDIM']*8))
        else:
            raise Exception("Not Implemented. So far only 8 byte floats are supported")
    def _web_repr_(self,name,namespace):
        s= "Inr Stream Writer Object: <br>"
        s += " + file: "+str(self.filename)+" <br>"
        s += " + length: "+str(self.image_i)+" <br>"
        if hasattr(self,'get_image'):
            s+= '<img class="mjpg" src="/mjpg/'+name+'" alt="'+name+'" height="400"/>'
        return s
    @property
    def buffered(self):
        return 0

class InrImageFileStreamer(object):
    def __init__(self,filenames):
        if type(filenames) is str:
            filenames = litus.natural_sorted(glob.glob(filenames))
        self.filenames = filenames
        self.lengths = []
        self.file_i = 0
        self.fileobject = None
        self.fileobject_index = None
        for i,f in enumerate(self.filenames):
            with InrImageStreamer(f) as ims:
                self.lengths.append(len(ims))
    def reset(self):
        self.file_i = 0
        self.image_i = 0
    def __iter__(self):
        def f():
            file_i = 0
            image_i = 0
            while file_i < len(self.filenames):
                ims = InrImageStreamer(self.filenames[file_i])
                image_i = 0
                try:
                    while True:
                        yield ims.read(image_i)
                        image_i += 1
                except StopIteration:
                    file_i+=1
            raise StopIteration()
        return f()
    def skip(self,f=0,i=0):
        self.file_i += f
        self.image_i += i
        self.seek(self.file_i, self.image_i)
    def seek(self,f,i):
        self.file_i = f
        self.image_i = i
        while self.image_i >= self.lengths[self.file_i]:
            self.image_i -= self.lengths[self.file_i]
            self.file_i += 1
            if self.file_i >= len(self.filenames):
                raise StopIteration()
    def read(self):
        if self.fileobject_index != self.file_i:
            self.fileobject = InrImageStreamer(self.filenames[self.file_i])
            self.fileobject_index = self.file_i
        return self.fileobject.read(self.image_i)
    def get_image(self):
        return self.fileobject.get_image()
    def __len__(self):
        return np.sum(self.lengths)
    def __getitem__(self,indx):
        if type(indx) is int:
            self.seek(f=0,i=indx)
            return self.read()
    def _web_repr_(self,name,namespace):
        s= "Inr Stream Object:<br>"
        s += " + file: "+str(self.filename)+" <br>"
        s += " + length: "+str(self.image_i)+" <br>"
        if hasattr(self,'get_image'):
            s+= '<img class="mjpg" src="/mjpg/'+name+'" alt="'+name+'" height="400"/>'
        return s
    @property
    def buffered(self):
        return 0


class Stream(object):
    """
        Stream Base Class

        Streams have to have methods to either `get()`
        or `put` a frame.
    """
    def __init__(self, size=(50,50), pixel_per_degree=10, t_zero = 0.0, t=0.0, dt=0.001):
        self.size = list(size)
        self.pixel_per_degree = pixel_per_degree
        self.t = t
        self.t_zero = t_zero
        self.dt = dt
    def time_to_bin(self,t):
        return (t-self.t_zero)/self.dt
    def __iter__(self):
        while True:
            self.t += self.dt
            yield np.zeros(self.size)
    def available(self,l=1):
        return True
    def get(self,i):
        self.t += i * self.dt
        return np.zeros([i]+self.size)
    def put(self,s):
        raise Exception("Not implemented for basic stream.")
    def close(self):
        pass
    def _web_repr_(self,name,namespace):
        import cgi
        s= "Image Stream Object:<br>"
        s+= " + class: "+cgi.escape(str(self.__class__))+"<br>"
        try:
            s+= " + time: "+str(self.t)+"<br>"
        except:
            pass
        try:
            s+= " + length: "+str(len(self))+"<br>"
        except:
            s+= " + length: -- <br>"
        if hasattr(self,'get_image'):
            s+= '<img class="mjpg" src="/mjpg/'+name+'" alt="'+name+'" height="400"/>'
        return s
    @property
    def buffered(self):
        return 0

class RandomStream(Stream):
    def __init__(self, size=(50,50), pixel_per_degree=10, level=1.0, mean=0.0):
        self.level = level
        self.mean = mean
        self.size = list(size)
        self.pixel_per_degree = pixel_per_degree
    def __iter__(self):
        while True:
            yield self.level * np.random.rand(*self.size)
    def available(self,l=1):
        return True
    def get_image(self):
        return self.mean + self.level * np.random.rand(*(self.size))
    def get(self,i):
        return self.mean + self.level * np.random.rand(*([i]+self.size))
    def put(self,s):
        raise Exception("Not implemented for read only stream.")

class SequenceStream(Stream):
    """ 3d Numpy array that represents a sequence of images"""
    def __init__(self, sequence=np.zeros((0,50,50)), size=None, pixel_per_degree=10, max_frames = 5000):
        self.size = sequence.shape[1:]
        self.pixel_per_degree = pixel_per_degree
        self.sequence = sequence
        self.i = 0
        self.max_frames = max_frames
    def __iter__(self):
        while len(self.sequence) < self.i:
            self.i += 1
            yield self.sequence[i-1]
    def __len__(self):
        return len(self.sequence)
    def available(self,l=1):
        return (len(self.sequence) - self.i) > l
    def get_image(self):
        try:
            if self.i < 1:
                return self.sequence[-1]
            return self.sequence[self.i]
        except:
            return np.zeros(self.sequence.shape[1:])
    def get(self,i):
        self.i += i
        return self.sequence[int(self.i-i):self.i]
    def put(self,s):
        if self.sequence.shape[1:] == s.shape[1:]:
            if len(self.sequence) + len(s) > self.max_frames:
                self.sequence = np.concatenate([self.sequence,s],axis=0)[-self.max_frames:]
            else:
                self.sequence = np.concatenate([self.sequence,s],axis=0)
        else:
            if len(s) > self.max_frames:
                self.sequence = s[-self.max_frames:]
            else:
                self.sequence = s

class RepeatingStream(Stream):
    def __init__(self, sequence=np.zeros((0,50,50)), size=None, pixel_per_degree=10):
        self.size = sequence.shape[1:]
        self.pixel_per_degree = pixel_per_degree
        self.sequence = sequence
        self.i = 0
    def __iter__(self):
        while True:
            self.i += 1
            while len(self.sequence) < self.i:
                self.i=0
            yield self.sequence[i-1]
    def available(self,l=1):
        return len(sequence) > 0
    def get_image(self):
        try:
            return self.sequence[self.i]
        except:
            return np.zeros(self.sequence.shape[1:])
    def get(self,i):
        self.i += i
        if len(self.sequence) < self.i:
            pre_index = int(self.i-i)
            self.i -= len(self.sequence)
            return np.concatenate([self.sequence[pre_index:],self.sequence[:self.i]],axis=0)
        return self.sequence[(self.i-i):self.i]
    def put(self,s):
        self.sequence = np.concatenate([self.sequence,s],axis=0.0)


class TimedSequenceStream(object):
    """ 3d Numpy array that represents a sequence of images"""
    def __init__(self, sequence=np.zeros((0,50,50)), size=None, pixel_per_degree=10, t_zero = 0.0, dt = 0.001):
        self.size = sequence.shape[1:]
        self.pixel_per_degree = pixel_per_degree
        self.sequence = sequence
        self.t_zero = t_zero
        self.dt = dt
    def time_to_bin(self,t1,t2):
        return (np.round((t1-self.t_zero)/self.dt),
                         np.round((t2-self.t_zero)/self.dt))
    def xs(self,t1,t2):
        return np.arange(np.round((t1-self.t_zero)/self.dt),
                         np.round((t2-self.t_zero)/self.dt))
    def ts(self,t1,t2):
        return self.dt*np.arange(np.round((t1-self.t_zero)/self.dt),
                         np.round((t2-self.t_zero)/self.dt),1.0)
    def available(self,t1,t2):
        b1,b2 = self.time_to_bin(t1,t2)
        return b1 >= 0 and b2 <= len(self.sequence)
    def get(self,t1,t2):
        b1,b2 = self.time_to_bin(t1,t2)
        return self.sequence[b1:b2]
    def get_tsvs(self,t1,t2):
        b1,b2 = self.time_to_bin(t1,t2)
        if b1 < 0:
            b1 = 0
        if b2 > len(self.sequence):
            b2 = len(self.sequence)
        ts = self.dt*np.arange(b1,b2,1.0)
        return ts,self.sequence[b1:b2]
    def put(self,t1,t2, s):
        b1,b2 = self.time_to_bin(t1,t2)
        self.sequence[b1:b2] = s
        
        
class TimedResampleStream(TimedSequenceStream):
    """ 3d Numpy array that represents a sequence of images"""
    def __init__(self, stream, t_zero = 0.0, dt = 0.001):
        self.stream = stream
        self.t_zero = t_zero
        self.dt = dt
    def time_to_bin(self,t1,t2):
        return (np.round((t1-self.t_zero)/self.dt),
                         np.round((t2-self.t_zero)/self.dt))
    def xs(self,t1,t2):
        return np.arange(np.round((t1-self.t_zero)/self.dt),
                         np.round((t2-self.t_zero)/self.dt))
    def available(self,t1,t2):
        return self.stream.available(t1,t2)
    def get_tsvs(self,t1,t2):
        return self.stream.get_tsvs(t1,t2)
    def get(self,t1,t2):
        t,v = self.stream.get_tsvs(t1-2.0*self.dt,t2+2.0*self.dt)
        try:
            return interp1d(t,
                        v.reshape(len(t),-1),
                        axis=0,
                        fill_value='extrapolate',
                        bounds_error = False
                       )(self.ts(t1,t2)).reshape(
            [len(self.ts(t1,t2))]+list(v.shape[1:]))
        except ValueError:
            # old versions of scipy don't know extrapolate
            # it also doesn't behave as numpy interpolate (extending the first and last values) as only one value is accepted
            # this should not be a problem if we 2*dt before and after the time slice
            return interp1d(t,
                        v.reshape(len(t),-1),
                        axis=0,
                        fill_value=np.mean(v),
                        bounds_error = False
                       )(self.ts(t1,t2)).reshape(
            [len(self.ts(t1,t2))]+list(v.shape[1:]))
    def put(self,t1,t2, s):
        self.stream.put(t1,t2)

_started_tkinter_main_loop = False
_main_root = None

class StreamVisualizer():
    def __init__(self):
        self.dirty = False
        self.refresh_rate = 0.001
        self.minimal_refresh_rate = 0.01
        self.last_buffer = []
        self.closed = False
        self.auto_scale_refresh_rate = True
        self._last_put = datetime.datetime.now()
        self.decay = 0.05
        self.decay_activity = None
        self.last_batch_length = None
        self.last_batch_time = None
        self.cmap = None
        #self.recieve_thread = thread.start_new_thread(self.recieve,tuple())
    def mainloop(self):
        try:
            import Tkinter as tk
        except ImportError:
            import tkinter as tk
        from PIL import Image, ImageTk
        from ttk import Frame, Button, Style
        import time
        import socket
        self.root = tk.Toplevel() #Tk()
        self.root.title('Display')
        self.image = Image.fromarray(np.zeros((200,200))).convert('RGB')
        self.image1 = ImageTk.PhotoImage(self.image)
        self.panel1 = tk.Label(self.root, image=self.image1)
        self.display = self.image1
        self.frame1 = Frame(self.root, height=50, width=50)
        self.panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        self.root.after(100, self.advance_image)
        self.root.after(100, self.update_image)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        #global _started_tkinter_main_loop
        #if not _started_tkinter_main_loop:
        #    _started_tkinter_main_loop = True
        #    print("Starting Tk main thread...")

    def on_closing(self):
        self.closed = True
        self.root.destroy()
    def put(self,img):
        if self.closed:
            pass #
        new_images = [i for i in img]
        self.last_buffer.extend(new_images)
        self.last_batch_length = len(new_images)
        if self.auto_scale_refresh_rate:
            self.last_batch_time = (datetime.datetime.now() - self._last_put).total_seconds()
            self.refresh_rate = self.last_batch_time/float(len(new_images))
            #print(self.refresh_rate)
        self._last_put = datetime.datetime.now()
        #if hasattr(self,'root'):
        #    self.root.title(str(len(self.last_buffer))+' Images buffered')
    def get_image(self):
        if self.decay_activity is not None:
            return self.decay_activity
        if len(self.last_buffer) > 0:
            return self.last_buffer[0]
        return np.zeros((50,50))
    def advance_image(self):
        from PIL import Image, ImageTk
        function_start = datetime.datetime.now()
        #refresh = (self.refresh_rate)
        half = len(self.last_buffer)*0.9
        num_frames = 0 # consume all
        #if self._last_put is not None and self.last_batch_length is not None and self.last_batch_time is not None:
        #    # only consume up to X images
        #    if self.last_batch_length > 0:
        #        num_frames = self.last_batch_length+((self._last_put - datetime.datetime.now()).total_seconds() + self.last_batch_time)/self.refresh_rate
        #while len(self.last_buffer) > 1.2*num_frames:
        for i in np.arange(np.floor(self.minimal_refresh_rate/self.refresh_rate)+1.0):
            if len(self.last_buffer) > 1:
                try:
                    image_buffer = self.last_buffer.pop(0) # take image from the front
                    if self.decay_activity is None:
                        self.decay_activity = 1.0*image_buffer
                    self.decay_activity -= self.decay * self.decay_activity
                    self.decay_activity += image_buffer
                    #refresh = self.image.info.get('refresh',refresh)
                except Exception as e:
                    #print(e)
                    raise
                    #pass
        function_lag = (datetime.datetime.now() - function_start).total_seconds()
        self.root.after(int(max((self.refresh_rate-function_lag),self.minimal_refresh_rate)*1000.0), self.advance_image)
    def update_image(self):
        from PIL import Image, ImageTk
        if self.decay_activity is not None:
            try:
                da = self.decay_activity
                da = da + np.min(da)
                im = da/max(np.max(da),1.0)
                im = im.clip(0.0,1.0)
                if im.shape[0] < 50:
                    im = np.repeat(im,10,axis=0)
                    im = np.repeat(im,10,axis=1)
                elif im.shape[0] < 100:
                    im = np.repeat(im,5,axis=0)
                    im = np.repeat(im,5,axis=1)
                elif im.shape[0] < 300:
                    im = np.repeat(im,2,axis=0)
                    im = np.repeat(im,2,axis=1)
                if self.cmap is not None:
                    self.image = Image.fromarray(self.cmap(im, bytes=True))
                else:
                    self.image = Image.fromarray(256.0*im).convert('RGB')
                #self.image.resize((500,500), Image.ANTIALIAS)
                #self.image.load()
                self.image1 = ImageTk.PhotoImage(self.image)
                self.panel1.configure(image=self.image1)
                self.root.title(str(len(self.last_buffer))+' Images buffered')
                self.display = self.image1
            except Exception as e:
                #print(e)
                raise
                #pass
        self.root.after(int(50), self.update_image)
    @property
    def buffered(self):
        return len(self.last_buffer)
    def _web_repr_(self,name,namespace):
        import cgi
        s= "Image Stream Object:<br>"
        s+= " + class: "+cgi.escape(str(self.__class__))+"<br>"
        try:
            s+= " + length: "+str(len(self))+"<br>"
        except:
            s+= " + length: -- <br>"
        if hasattr(self,'get_image'):
            s+= '<img class="mjpg" class="mjpg" src="/mjpg/'+name+'" alt="'+name+'" height="400"/>'
        return s
    def _web_repr_status_(self,name,namespace):
        import cgi
        s= ""
        try:
            s+= " + time: "+str(self.t)+"<br>"
        except:
            pass
        return s
def _create_mainloop():
    try:
        import Tkinter as tk
    except ImportError:
        import tkinter as tk
    global _main_root
    _main_root = tk.Tk()
    _main_root.title('Hidden Display')
    _main_root.withdraw()
    _started_tkinter_main_loop = True
    print("Starting Tk main thread...")
    _main_root.mainloop()    

try:
    import time,datetime
    import wx
    import numpy as np
    class WXImageDisplay(wx.App):
        def __init__(self, redirect=False, filename=None):
            wx.App.__init__(self, redirect, filename)
            self.array = np.random.rand(10,100,100,3)
            self.t=0
            self.frame = wx.Frame(None, title='Photo Control')
            self.panel = wx.Panel(self.frame)

            self.PhotoMaxSize = 240

            self.createWidgets()
            self.frame.Show()
            self.frame.Bind(wx.EVT_SIZE, self.OnSize)
        def OnSize(self, event):
            self.panel.Layout()
            self.panel.Refresh()
        def createWidgets(self):
            img = wx.EmptyImage(240,240)
            self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, 
                                             wx.BitmapFromImage(img))
            #browseBtn = wx.Button(self.panel, label='Button')
            #browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)
            self.mainSizer = wx.BoxSizer(wx.VERTICAL)
            self.sizer = wx.BoxSizer(wx.HORIZONTAL)
            self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                               0, wx.ALL|wx.EXPAND, 5)
            self.mainSizer.Add(self.imageCtrl, 0, wx.ALL|wx.EXPAND, 5)
            self.mainSizer.Add(self.sizer, 0, wx.ALL|wx.EXPAND, 5)
            self.panel.SetSizer(self.mainSizer)
            #self.sizer.Add(browseBtn, 0, wx.ALL|wx.EXPAND, 5)
            self.mainSizer.Fit(self.frame)
            #self.frame.SetAutoLayout(1) 
            self.panel.Layout()
            #self.onView()
        def onBrowse(self, event):
            """ 
            Browse for file
            """ 
            try:
                self.onView()
            except Exception as e:
                print(e)
                pass
        def display(self, im):
            if len(im.shape) == 2:
                im = np.repeat(im[:,:,None],3,axis=2)
            array = 256*im
            array = np.array(array,dtype='uint8')
            width,height,chnls = array.shape
            image = wx.EmptyImage(width,height)
            image.SetData( array.tostring())
            wxBitmap = image.ConvertToBitmap()
            img = image
            # scale the image, preserving the aspect ratio
            W = img.GetWidth()
            H = img.GetHeight()
            if W > H:
                NewW = self.PhotoMaxSize
                NewH = self.PhotoMaxSize * H / W
            else:
                NewH = self.PhotoMaxSize
                NewW = self.PhotoMaxSize * W / H
            img = img.Scale(NewW,NewH)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            self.panel.Refresh()
        def onView(self):
            array = 256*self.array[self.t%len(self.array),:,:,:]
            self.t+=1
            array = np.array(array,dtype='uint8')
            width,height,chnls = array.shape
            image = wx.EmptyImage(width,height)
            image.SetData( array.tostring())
            wxBitmap = image.ConvertToBitmap()
            img = image
            # scale the image, preserving the aspect ratio
            W = img.GetWidth()
            H = img.GetHeight()
            if W > H:
                NewW = self.PhotoMaxSize
                NewH = self.PhotoMaxSize * H / W
            else:
                NewH = self.PhotoMaxSize
                NewW = self.PhotoMaxSize * W / H
            img = img.Scale(NewW,NewH)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            self.panel.Refresh()
    _refs = []
    class NewStreamVisualizer():
        def __init__(self):
            self.array = np.random.rand(10,20,20,3)
            _refs.append(self)
            self.t = 0
            self.dirty = False
            self.refresh_rate = 0.001
            self.minimal_refresh_rate = 0.01
            self.last_buffer = []
            self.closed = False
            self.auto_scale_refresh_rate = True
            self._last_put = datetime.datetime.now()
            self.decay = 0.05
            self.decay_activity = None
            self.last_batch_length = None
            self.last_batch_time = None
            self.cmap = None
            self.backend = None
            #self.recieve_thread = thread.start_new_thread(self.recieve,tuple())
            try:
                import thread
            except ImportError:
                import _thread as thread
            self.thread1 = thread.start_new_thread(self.mainloop,tuple())
            time.sleep(0.1)
            self.thread2 = thread.start_new_thread(self.processloop,tuple())
            time.sleep(0.1)
        def __del__(self):
            pass
            #self.closed = True
            #self.backend = None
        def mainloop(self):
            self.backend = WXImageDisplay()
            self.backend.MainLoop()
        def processloop(self):
            while not self.closed:
                if not self.closed:
                    #self.advance_image()
                    #self.update_image()
                    self.display(self.array[self.t%self.array.shape[0]])
                    self.t+=1
                try:
                    time.sleep(0.01)#float(getattr(self,'refresh_rate',0.01)))
                except:
                    time.sleep(0.01)
        def display(self, ar):
            if self.backend is not None:
                wx.CallAfter(self.backend.display,(ar))
        def on_closing(self):
            self.closed = True
            if self.backend is not None:
                self.backend.destroy()
        def put(self,img):
            if self.closed:
                pass #
            if self.backend is not None:
                if len(self.array.shape) == 4:
                    self.array = np.concatenate([self.array,
                                    np.array([i if len(i.shape) == 3 else i[:,:,None] for i in img])], axis=0)
                else:
                    self.array = np.concatenate([self.array,
                                    np.array([i for i in img])], axis=0)
            self._last_put = datetime.datetime.now()
        def get_image(self):
            if self.decay_activity is not None:
                return self.decay_activity
            if len(self.last_buffer) > 0:
                return self.last_buffer[0]
            return np.zeros((50,50))
        def advance_image(self):
            function_start = datetime.datetime.now()
            half = len(self.last_buffer)*0.9
            num_frames = 0 # consume all
            for i in np.arange(np.floor(self.minimal_refresh_rate/self.refresh_rate)+1.0):
                if len(self.last_buffer) > 1:
                    image_buffer = self.last_buffer.pop(0) # take image from the front
                    if self.decay_activity is None:
                        self.decay_activity = 1.0*image_buffer
                    self.decay_activity -= self.decay * self.decay_activity
                    self.decay_activity += image_buffer
            function_lag = (datetime.datetime.now() - function_start).total_seconds()
        def update_image(self):
            if self.decay_activity is not None:
                    da = self.decay_activity
                    da = da + np.min(da)
                    im = da/max(np.max(da),1.0)
                    im = im.clip(0.0,1.0)
                    if im.shape[0] < 50:
                        im = np.repeat(im,10,axis=0)
                        im = np.repeat(im,10,axis=1)
                    elif im.shape[0] < 100:
                        im = np.repeat(im,5,axis=0)
                        im = np.repeat(im,5,axis=1)
                    elif im.shape[0] < 300:
                        im = np.repeat(im,2,axis=0)
                        im = np.repeat(im,2,axis=1)
                    if self.cmap is not None:
                        self.display(self.cmap(im, bytes=True))
                    else:
                        self.display(256.0*im)
        @property
        def buffered(self):
            return len(self.last_buffer)
        def _web_repr_(self,name,namespace):
            import cgi
            s= "Image Stream Object:<br>"
            s+= " + class: "+cgi.escape(str(self.__class__))+"<br>"
            try:
                s+= " + length: "+str(len(self))+"<br>"
            except:
                s+= " + length: -- <br>"
            if hasattr(self,'get_image'):
                s+= '<img class="mjpg" class="mjpg" src="/mjpg/'+name+'" alt="'+name+'" height="400"/>'
            return s
        def _web_repr_status_(self,name,namespace):
            import cgi
            s= ""
            try:
                s+= " + time: "+str(self.t)+"<br>"
            except:
                pass
            return s
except:
    WXImageDisplay = None


def run_visualizer():
    try:
        import thread
    except ImportError:
        import _thread as thread
    import time
    global _main_root
    if _main_root is None:
        thread.start_new_thread(_create_mainloop,tuple())
        time.sleep(0.1)
    s = StreamVisualizer()
    thread.start_new_thread(s.mainloop,tuple())
    return s

class StreamToNetwork(Stream):
    def __init__(self,port,host='localhost',compress_level=0,resize=(1.0,1.0)):
        self.port = port
        self.host = host
        self.compress_level=compress_level
        self.resize = resize
    def put(self,s):
        from . import png
        png.png_client(s,info={},port=self.port,host=self.host,compress_level=self.compress_level,resize=self.resize)

try:
    import h5py
    class HDF5Reader(Stream):
        def __init__(self,filename,data_set_name='images'):
            self.file = h5py.File(filename, "r") 
            self.data_set_name = data_set_name
            self.dset = self.file[data_set_name]
            self.i = 0
        def get(self,i=1):
            d = self.dset[self.i:self.i+i]
            self.i += i
            return d
    class HDF5Writer(Stream):
        def __init__(self,filename,data_set_name='images',size=None):
            self.filename = filename
            #self.file = h5py.File(filename, "r+") 
            self.data_set_name = data_set_name
            if size is not None:
                with h5py.File(self.filename, "a") as f:
                    self.dset = self.file.create_dataset(data_set_name, 
                                (0,size[0],size[1]), 
                                compression="gzip",
                                chunks=(100,size[0],size[1]),
                                maxshape=(None,s.shape[1],s.shape[2]),
                                dtype='f')
        def put(self,s):
            with h5py.File(self.filename, "a") as f:
                print(set(f.keys()))
                if not self.data_set_name in set(f.keys()):
                    self.dset = f.create_dataset(self.data_set_name, 
                                (0,s.shape[1],s.shape[2]),
                                compression="gzip",
                                chunks=(200,s.shape[1],s.shape[2]),
                                maxshape=(None,s.shape[1],s.shape[2]),
                                dtype='f')
                else:
                    self.dset = f[self.data_set_name]
                assert len(s.shape) == 3
                assert s.shape[1] == self.dset.shape[1]
                assert s.shape[2] == self.dset.shape[2]
                self.dset.resize(self.dset.shape[0] + s.shape[0],axis=0)
                self.dset[-s.shape[0]:,:,:] = s
except:
    class HDF5Reader(Stream):
        def __init__(self,*args,**kwargs):
            raise Exception('h5py needs to be installed!')

    class HDF5Writer(Stream):
        def __init__(self,*args,**kwargs):
            raise Exception('h5py needs to be installed!')

class NumpyReader(Stream):
    pass

class NumpyWriter(Stream):
    pass


class VideoReader(Stream):
    def __init__(self,filename=0,size=(50,50),offset=None,dt=1.0/24.0):
        """
            `filename` can be either a device number or the path to a video file.
            The file will be opened as such: `cv2.VideoCapture(filename)`

            If only one camera is connected, it can be selected with `0`.
            If more than one camera is connected, 


        """
        
        try:
            import cv2
        except:
            print(""" OpenCV has to be installed for video input """)
            raise
        self.cv2_module = cv2
        self.size =size
        self.offset = offset
        self.mode = 'mean'
        self.cap = cv2.VideoCapture(filename)
        self.dt = dt
        self.i = 0
        self.last_image = np.zeros(self.size)
        #frames = np.asarray([np.asarray(f) for f in v[i]])
    def __len__(self):
        return len(self.sequence)
    def get_one_frame(self):
        try:
            ret, frame = self.cap.read()
            offset = self.offset
            if self.offset is None:
                offset = (int(np.floor((frame.shape[0]-self.size[0])/2.0)),
                          int(np.floor((frame.shape[1]-self.size[1])/2.0)))
            if self.mode == 'mean':
                return frame[offset[0]:(offset[0]+self.size[0]),
                                    offset[1]:(offset[1]+self.size[1])].mean(2)
            if self.mode == 'r':
                return frame[offset[0]:(offset[0]+self.size[0]),
                                    offset[1]:(offset[1]+self.size[1]),0]
            if self.mode == 'g':
                return frame[offset[0]:(offset[0]+self.size[0]),
                                    offset[1]:(offset[1]+self.size[1]),1]
            if self.mode == 'b':
                return frame[offset[0]:(offset[0]+self.size[0]),
                                    offset[1]:(offset[1]+self.size[1]),2]
            return frame[offset[0]:(offset[0]+self.size[0]),
                                offset[1]:(offset[1]+self.size[1])]
        except:
            return np.zeros(self.size)
    def get_image(self):
        return self.last_image
    def get(self,i):
        self.i += i
        frames = np.asarray([self.get_one_frame() for f in range(i)])
        self.last_image = frames[-1]
        return frames
    def close(self):
        self.cap.release()


class VideoWriter(Stream):
    def __init__(self,filename='output.avi',size=(50,50),codec='XVID', isColor=False):
        """
            possible `codec`s: 'DIVX', 'XVID', 'MJPG', 'X264', 'WMV1', 'WMV2'

        """
        try:
            import cv2
        except:
            print(""" OpenCV has to be installed for video output """)
            raise
        fourcc = cv2.VideoWriter_fourcc(*codec)
        self.out = cv2.VideoWriter()
        self.out.open(filename,fourcc, fps=20.0, frameSize=size, isColor=isColor)
    def put(self,s):
        for frame in s:
            self.last_image = frame
            self.out.write(np.uint8(frame))
    def close(self):
        self.out.release()

class ImageSequence(Stream):
    """loads a sequence of images

    """
    def __init__(self,filenames='*.jpg',size=(50,50),repeats=0,offset=None,isColor=False):
        self.repeats = repeats
        self.offset = offset
        self.i=0
        if type(filenames) is str:
            import glob
            self.file_list = sorted(glob.glob(filenames))
        elif type(filenames) is list:
            self.file_list = filenames
        else:
            raise Exception('filenames not recognized. Has to be a string or list.')
        super(ImageSequence,self).__init__()
    def __len__(self):
        return len(self.file_list)
    def get_one_frame(self):
        from PIL import Image
        try:
            frame = np.array(Image.open(self.file_list[self.i]))
            offset = self.offset
            if self.offset is None:
                offset = (int(np.floor((frame.shape[0]-self.size[0])/2.0)),
                          int(np.floor((frame.shape[1]-self.size[1])/2.0)))
            return frame[offset[0]:(offset[0]+self.size[0]),
                            offset[1]:(offset[1]+self.size[1])].mean(2)
        except:
            return np.zeros(self.size)  
    def get_image(self):
        return self.last_image
    def get(self,i):
        self.i += i
        frames = np.asarray([self.get_one_frame() for f in range(i)])
        self.last_image = frames[-1]
        return frames
    
