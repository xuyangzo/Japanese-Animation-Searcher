import imageio
import os


"""
Convert single .jpg/.png to .gif
"""
def ConvertSingleGIF(gif_name, path, new_path):
    frames = []
    frames.append(imageio.imread(path))
    imageio.mimsave(new_path+gif_name, frames, "GIF")

    return


"""
Convert a series of images from .jpg/.png to .gif
Not used in 番号搜索器
"""
def ConvertSeriesGIF(gif_name, path):
    frames = []
    jpgFiles = os.listdir(path)
    image_list = [os.path.join(path, f) for f in jpgFiles]
    for name in image_list:
        frames.append(imageio.imread(name))
    imageio.mimsave(gif_name, frames, "GIF")

    return


"""
Go through all the downloaded image
"""
def ConvertAll(path, new_path):

    jpgFiles = os.listdir(path)

    # declare new path to save images
    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    for singleFile in jpgFiles:
        ConvertSingleGIF(singleFile[:-3]+"gif", path+singleFile, new_path)


"""
Declare main() only for test
"""
def main():
    current_path = os.path.dirname(__file__)
    parent_path = os.path.dirname(current_path)
    path = parent_path + "/images/"
    new_path = parent_path + "/ConvetedImages/"
    ConvertAll(path, new_path)

if __name__ == "__main__":
    main()