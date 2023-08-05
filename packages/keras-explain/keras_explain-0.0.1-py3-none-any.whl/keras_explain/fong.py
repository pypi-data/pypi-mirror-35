import torch
from keras.applications import VGG16
from torch.autograd import Variable

import cv2
import numpy as np

use_cuda = torch.cuda.is_available()
FloatTensor = torch.cuda.FloatTensor if use_cuda else torch.FloatTensor
LongTensor = torch.cuda.LongTensor if use_cuda else torch.LongTensor
Tensor = FloatTensor

class FongPerturb:

    name = "FongPerturb"

    def __init__(self):
        pass

    @staticmethod
    def tv_norm(input, tv_beta):
        img = input[0, 0, :]
        row_grad = torch.mean(torch.abs((img[:-1, :] - img[1:, :])).pow(tv_beta))
        col_grad = torch.mean(torch.abs((img[:, :-1] - img[:, 1:])).pow(tv_beta))
        return row_grad + col_grad

    @staticmethod
    def preprocess_image(img):
        preprocessed_img = img.copy()[:, :, :]

        preprocessed_img = \
            np.ascontiguousarray(np.transpose(preprocessed_img, (2, 0, 1)))

        if use_cuda:
            preprocessed_img_tensor = torch.from_numpy(preprocessed_img).cuda()
        else:
            preprocessed_img_tensor = torch.from_numpy(preprocessed_img)

        preprocessed_img_tensor.unsqueeze_(0)
        return Variable(preprocessed_img_tensor, requires_grad=False)

    @staticmethod
    def save(mask, img, blurred):
        mask = mask.cpu().data.numpy()[0]
        mask = np.transpose(mask, (1, 2, 0))

        mask = (mask - np.min(mask)) / np.max(mask)
        mask = 1 - mask
        heatmap = cv2.applyColorMap(np.uint8(255 * mask), cv2.COLORMAP_JET)

        heatmap = np.float32(heatmap) / 255
        cam = 1.0 * heatmap + np.float32(img) / 255
        cam = cam / np.max(cam)

        img = np.float32(img) / 255
        perturbated = np.multiply(1 - mask, img) + np.multiply(mask, blurred)

        # cv2.imwrite("perturbated.png", np.uint8(255 * perturbated))
        # cv2.imwrite("heatmap.png", np.uint8(255 * heatmap))
        # cv2.imwrite("mask.png", np.uint8(255 * mask))
        # cv2.imwrite("cam.png", np.uint8(255 * cam))
        return mask

    @staticmethod
    def numpy_to_torch(img, requires_grad=True):
        if len(img.shape) < 3:
            output = np.float32([img])
        else:
            output = np.transpose(img, (2, 0, 1))

        output = torch.from_numpy(output)
        if use_cuda:
            output = output.cuda()

        output.unsqueeze_(0)
        v = Variable(output, requires_grad=requires_grad)
        return v

    @staticmethod
    def numpy_to_torch2(img, requires_grad=False):

        output = torch.from_numpy(img)
        if use_cuda:
            output = output.cuda()

        v = Variable(output, requires_grad=requires_grad)
        return v

    def explain(self, image, predictor, target_class, all_images=None,
                    **kwargs):
        # Hyper parameters.
        # TODO: remove cv2
        # TODO: try to rewrite to keras or tf
        tv_beta = 3
        learning_rate = 0.1
        max_iterations = 500
        l1_coeff = 0.01
        tv_coeff = 0.2

        model = kwargs["model"]
        original_img = image
        img = np.float32(original_img)
        img_copy = original_img.copy()
        img_copy = np.uint8(model.deprocess_image(img_copy) * 255)
        blurred_img2 = model.preprocess_image(
            np.float32(cv2.medianBlur(img_copy, 11)))
        mask_init = np.ones((28, 28), dtype=np.float32)

        # Convert to torch variables
        img = self.preprocess_image(img)
        print(img.shape)
        blurred_img = self.preprocess_image(blurred_img2)
        mask = self.numpy_to_torch(mask_init)

        if use_cuda:
            upsample = torch.nn.UpsamplingBilinear2d(
                size=model.input_size).cuda()
        else:
            upsample = torch.nn.UpsamplingBilinear2d(size=model.input_size)
        optimizer = torch.optim.Adam([mask], lr=learning_rate)

        temp_img = np.rollaxis(img.data.numpy(), 1, 4)
        target = predictor(temp_img)
        category = np.argmax(target)
        print("Category with highest probability", category)
        print("Optimizing.. ")

        for i in range(max_iterations):
            upsampled_mask = upsample(mask)
            # The single channel mask is used with an RGB image,
            # so the mask is duplicated to have 3 channel,
            upsampled_mask = \
                upsampled_mask.expand(1, 3, upsampled_mask.size(2),
                                      upsampled_mask.size(3))

            # Use the mask to perturbated the input image.
            perturbated_input = img.mul(upsampled_mask) + \
                                blurred_img.mul(1 - upsampled_mask)

            noise = np.zeros(list(model.input_size) + [3], dtype=np.float32)
            noise = noise + cv2.randn(noise, 0, 0.2)
            noise = self.numpy_to_torch(noise)
            perturbated_input = perturbated_input + noise

            temp_img = np.rollaxis(perturbated_input.data.numpy(), 1, 4)
            outputs = self.numpy_to_torch2(predictor(temp_img))

            loss = l1_coeff * torch.mean(torch.abs(1 - mask)) + \
                   tv_coeff * self.tv_norm(mask, tv_beta) + outputs[0, category]

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Optional: clamping seems to give better results
            mask.data.clamp_(0, 1)
            print(i)

        upsampled_mask = upsample(mask)

        mask = upsampled_mask.cpu().data.numpy()[0]
        mask = np.transpose(mask, (1, 2, 0))

        print(mask.min())
        print(mask.max())

        mask = (mask - np.min(mask)) / np.max(mask)
        mask = 1 - mask
        mask = mask[:, :, 0]

        print(mask.min())
        print(mask.max())

        return mask, None
