# import cv2

# def remove_people(rgb_path, mask_path, output_path):
#     # Read the RGB image
#     rgb_image = cv2.imread(rgb_path)

#     # Read the binary mask image
#     mask_image = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

#     # Invert the mask (assuming white represents people)
#     mask_image = cv2.bitwise_not(mask_image)

#     # Apply the mask to the RGB image
#     result_image = cv2.bitwise_and(rgb_image, rgb_image, mask=mask_image)

#     # Save the resulting image
#     cv2.imwrite(output_path, result_image)

# # Paths to the input RGB image and the binary mask image
# rgb_path = "rgb/1311870517.385883.png"
# mask_path = "output/1311870517.385883.png"

# # Output path for the resulting image
# output_path = "removed/1311870517.385883.png"

# # Remove people from the RGB image using the mask
# remove_people(rgb_path, mask_path, output_path)

# print("People removed and saved as:", output_path)

import os
import cv2

def remove_people(rgb_folder, output_folder):
    # Iterate over all files in the rgb folder
    for filename in os.listdir(rgb_folder):
        if filename.endswith(".png"):
            # Construct the paths for RGB image and corresponding mask image
            rgb_path = os.path.join(rgb_folder, filename)
            mask_path = os.path.join("output", filename)  # Assuming mask images are in the "output" folder

            # Check if the mask image exists
            if os.path.exists(mask_path):
                # Read the RGB image
                rgb_image = cv2.imread(rgb_path)

                # Read the binary mask image
                mask_image = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

                # Invert the mask (assuming white represents people)
                mask_image = cv2.bitwise_not(mask_image)

                # Apply the mask to the RGB image
                result_image = cv2.bitwise_and(rgb_image, rgb_image, mask=mask_image)

                # Output path for the resulting image
                output_path = os.path.join(output_folder, filename)

                # Save the resulting image
                cv2.imwrite(output_path, result_image)

                print("People removed from", filename, "and saved as:", output_path)
            else:
                print("No corresponding mask found for", filename)

# Paths to the folders
rgb_folder = "rgb"
output_folder = "removed"

# Remove people from images in the "rgb" folder using corresponding masks in the "output" folder
remove_people(rgb_folder, output_folder)
