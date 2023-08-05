
Operation method :
  
    Bofore Operation install "flv2img":
    pip install flv2img0.1.4



    flv2img:
        input£ºflv(Video path),rate(How many frames per second),star(the start of frames you want),end(the end of frames you want)
        python 
                from flv2img import flv2img
                flv2img.flv2img(flv,rate,star,end)
        output£ºlist_all(list of image£©
        PS:Video converted to image 

    faceimg:
        input£ºflv(Video path),rate(How many frames per second),star(the start of frames you want),end(the end of frames you want)
        python 
                from flv2img import flv2img
                flv2img.faceimg(flv,rate,star,end)
        output£ºface_list(list of image£©
        PS:Video converted to image with face
