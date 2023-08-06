import steg_img

s = steg_img.IMG(payload_path='./test_data/payload.txt', image_path='/Users/andrewscott/Desktop/markus-spiske-445253-unsplash.png')
s.hide()

s_prime = steg_img.IMG(image_path='./new.png')
s_prime.extract()