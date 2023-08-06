import os
import subprocess
import matplotlib.pyplot as plt
from IPython.display import HTML,display

def open_movie(path_to_movie,default_player = True,output_notebook = False):
    '''
    Open a movie that has already been rendered.
    Parameters
    ===========================================================
    path_to_movie - Relative path to your movie file
    default_player = True - Open with your default media player
    output_notebook = False - Open in a Jupyter notebook
    '''
    
    if default_player == True:
        subprocess.call(['open',str(path_to_movie)])
    if output_notebook == True:
        display(HTML("""
            <video width="500" height="500" controls>
              <source src="%(file)s">
            </video>
            """ % {"file":path_to_movie}))

class Movie():
    def __init__(self,name='movie',framerate = 10,file_type='.png',movie_type = '.avi',verbose = False, save_images = False):
        '''
        Initialize your movie
        Parameters
        ===========================================================
        name = 'movie' - Name of your movie.
        framerate = 10 - Framerate of your movie.
        file_type = '.png - Image file types.
        movie_type = '.avi' - Movie file type.
        verbose = False - Display FFMPEG output.
        save_images = False - Save images produced by pyvie.
        '''
        
        self.counter = 0
        self.name = name
        self.file_type = file_type
        self.framerate = framerate
        self.files = []
        self.ext = movie_type
        self.verbose = verbose
        self.save_images = save_images
        
        if os.path.isfile(str(self.name)+str(self.ext)):
            numb = 0
            exists = os.path.isfile(str(self.name)+str(self.ext))
            while exists == True:
                numb += 1
                exists = os.path.isfile(str(self.name)+'-'+str(numb)+str(self.ext))
            self.name = str(self.name)+'-'+str(numb)
    def gather(self,*args,**kwargs):
        '''
        Add frames to the movie
        '''
       
        plt.savefig(str(self.name)+'_frame'+str('%04d' % self.counter)+str(self.file_type),*args,**kwargs)
        self.files.append(str(self.name)+'_frame'+str('%04d' % self.counter)+str(self.file_type))
        self.counter += 1
    def finalize(self,open_movie=False,output_notebook=False):
        '''
        Create the movie
        Parameters
        ===========================================================
        open_movie - Opens new movie file with default media player
        output_notebook - Open file in Jupyter notebook
        '''
        if self.verbose == True:
            subprocess.call(["ffmpeg","-framerate", str(self.framerate), "-i",str(self.name)+"_frame%04d"+str(self.file_type), "-c:v", "mjpeg", "-qscale:v", "0", str(self.name)+str(self.ext)])
        
        else:
            subprocess.call(["ffmpeg","-loglevel","panic","-framerate", str(self.framerate), "-i",str(self.name)+"_frame%04d"+str(self.file_type), "-c:v", "mjpeg", "-qscale:v", "0", str(self.name)+str(self.ext)])
        
        if self.save_images == False:
            for f in self.files:
                os.remove(f)
        if open_movie == True:
            subprocess.call(['open',str(self.name)+str(self.ext)])
        if output_notebook == True:
            display(HTML("""
            <video width="500" height="500" controls>
              <source src="%(file)s">
            </video>
            """ % {"file":str(self.name)+str(self.ext)}))