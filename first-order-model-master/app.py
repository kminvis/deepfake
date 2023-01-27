import streamlit as st 
import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

source_image = imageio.imread('https://upload.wikimedia.org/wikipedia/commons/0/0f/IU_posing_for_Marie_Claire_Korea_March_2022_issue_03.jpg')
target_video = imageio.mimread('https://media.tenor.com/FarvZ15gb24AAAAd/ahegao.gif')
source_image = resize(source_image, (256, 256))[..., :3]
target_video = [resize(frame, (256, 256))[..., :3] for frame in target_video]

# from part_swap import load_checkpoints

# reconstruction_module, segmentation_module = load_checkpoints(config='config/vox-256-sem-15segments.yaml', 
#                                                checkpoint='/content/gdrive/My Drive/DeepFake/vox-15segments.pth.tar',
#                                                blend_scale=1)

# from part_swap import make_video

# predictions = make_video(swap_index=[1,2,4,9,10,11,12,13,14], source_image = source_image, target_video = target_video,
#                              segmentation_module=segmentation_module, reconstruction_module=reconstruction_module)

# def display(source, target, generated=None):
#     fig = plt.figure(figsize=(8 + 4 * (generated is not None), 6))

#     ims = []
#     for i in range(len(target)):
#         cols = [source]
#         cols.append(target[i])
#         if generated is not None:
#             cols.append(generated[i])
#         im = plt.imshow(np.concatenate(cols, axis=1), animated=True)
#         plt.axis('off')
#         ims.append([im])

#     ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
#     plt.close()
#     return ani

# response = HTML(display(source_image, target_video, predictions).to_html5_video())
st.write(source_image)
