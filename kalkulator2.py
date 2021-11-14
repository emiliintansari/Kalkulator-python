from tkinter import *

def MyCalc(source, side):
    sObj = Frame(source, borderwidth=4, bd=4, bg='Aquamarine') #merubah warna bg bagian tombol
    sObj.pack(side=side, expand=YES, fill=BOTH)
    return sObj

def tombol(source, side, text, command=None, bg='Aquamarine'): #merubah warna bg bagian tombol
    sObj = Button(source, text=text, command=command, bg=bg)
    sObj.pack(side=side, expand=YES, fill=BOTH)
    return sObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'Script  25 ') #ini buat ganti jenis tulisan 
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Kalkulatorku')

        display = StringVar()
        Entry(self, relief=FLAT, textvariable=display, bd=30, bg='Azure').pack(side=TOP, expand=YES, fill=BOTH) # buat ngerubah warna bagian atas 

        for TombAngka in ('123', '456', '789', '.0+', '/*-'): #buat urutan angka
            fNum = MyCalc(self, BOTTOM) #buat ngerubah posisi angka 
            for isdm in TombAngka:
                tombol(fNum, LEFT, isdm, lambda sObj=display, q=isdm: sObj.set(sObj.get() + q),bg='Cadet Blue') #buat ngerubah warna bagian simbol 

        for TombolC in (['C']):
            ers = MyCalc(self, RIGHT) #BUAT NGERUBAH POSISI TOMBOL KANAN DAN KIRI 
            for ichar in TombolC:
                tombol(ers, RIGHT, ichar, lambda sObj=display, q=ichar: sObj.set(''), bg='Dark Cyan')
        
        SamaDengan = MyCalc(self, LEFT)
        for sd in '=':
            if sd == '=':
                TombolSama = tombol(SamaDengan, LEFT, sd) 
                TombolSama.bind('<ButtonRelease-1>', lambda e,s=self, sObj=display: s.hitung(sObj), '+')
            else:
                TombolSama = tombol(SamaDengan, LEFT, sd, lambda sObj=display, s=' %s ' % sd: sObj.set(sObj.get()+s))
        
    def hitung(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('ERROR')

if __name__=='__main__':
    Tk.mainloop(app())