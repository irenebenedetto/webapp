import streamlit as st
import io
import numpy as np
from torchvision import transforms
from style_transfer.utils import *
def app():



    st.title('Style transfer')
    st.write("This is an unofficial implementation of [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576) for style transfer. Upload a content image and change its style with another one.")

    col1, col2 = st.columns(2)
    uploaded_file_style = col1.file_uploader("Upload an image for style", type=['png', 'jpg'])
    uploaded_file_content = col2.file_uploader("Upload an image for content", type=['png', 'jpg'])

    exp = st.expander('Parameters for style transfer')

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    cnn = models.vgg19(pretrained=True).features.to(device).eval()

    norm_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
    norm_std = torch.tensor([0.229, 0.224, 0.225]).to(device)


    num_steps = exp.slider('Select the number of iterations:', 100, 500, 250, 10)
    imsize = exp.selectbox('Select the size (pixel) of the output image:', options=[128, 256, 512])


    if uploaded_file_style is not None and uploaded_file_content is not None:
        bytes_data = uploaded_file_style.getvalue()
        style_img = Image.open(io.BytesIO(bytes_data)).convert('RGB').resize((256, 256))

        bytes_data = uploaded_file_content.getvalue()
        content_img = Image.open(io.BytesIO(bytes_data)).convert('RGB').resize((256, 256))
        col1, col2 = st.columns(2)
        col1.image(style_img, caption='Style image uploaded')
        col2.image(content_img, caption='Content image uploaded')

        content_img = transforms.ToTensor()(content_img).unsqueeze(0)
        style_img = transforms.ToTensor()(style_img).unsqueeze(0)
        input_img = content_img.clone()


        model, style_losses, content_losses = initialize_model_losses(cnn, norm_mean, norm_std, style_img, content_img)
        optimizer = optimizer = optim.LBFGS([input_img.requires_grad_()])

        style_weight, content_weight = 1000000, 1

        button = st.button('Transfer style')
        latest_iteration = st.empty()
        run = [0]
        pb = 0
        if button:
            bar = st.progress(0)

            while run[0] <= num_steps:
                bar.progress(run[0]/num_steps)
                pb +=1
                def closure():
                    # correct the values of updated input image
                    input_img.data.clamp_(0, 1)

                    optimizer.zero_grad()
                    model(input_img)
                    style_score = 0
                    content_score = 0

                    for sl in style_losses:
                        style_score += sl.loss
                    for cl in content_losses:
                        content_score += cl.loss

                    style_score *= style_weight
                    content_score *= content_weight

                    loss = style_score + content_score
                    loss.backward()

                    run[0] += 1

                    return style_score + content_score

                optimizer.step(closure)

            input_img.data.clamp_(0, 1)

            output = 255. * input_img.squeeze(0).permute(1, 2, 0).cpu().detach().numpy()
            output = Image.fromarray((output).astype(np.uint8), mode='RGB')
            
            bar.empty()
            st.subheader('Output image')
            st.image(output)
