from PIL import Image
import numpy as np

def swap_pixel_values(image_path,output_path):
    """
    Swaps the pixel values at coordinates (x1, y1) and (x2, y2) in the image array.
    """
    image = Image.open(image_path)
    image_array = np.array(image)
    swap=image_array
    height, width = image_array.shape[:2]  # Get image dimensions
    
    print("Enter the pixel values you want to swap as coordinates like (x1, y1) and (x2, y2).")
    x1 = int(input("Enter the value of x1: "))
    y1 = int(input("Enter the value of y1: "))
    x2 = int(input("Enter the value of x2: "))
    y2 = int(input("Enter the value of y2: "))

    # Check if coordinates are within the bounds of the image
    if (0 <= x1 < width and 0 <= y1 < height and 0 <= x2 < width and 0 <= y2 < height):
        temp = swap[y1, x1].copy()
        swap[y1, x1] = swap[y2, x2]
        swap[y2, x2] = temp

        swap_image = Image.fromarray(swap.astype('uint8'))
        swap_image.save(output_path)
        print(f"Pixels swapped and saved to {output_path}")
    else:
        print("One or more coordinates are out of bounds. Please enter valid coordinates.")
        return swap_pixel_values(image_path,output_path)

    
def apply_operation(image_path,output_path):
    """
    Applies a basic mathematical operation to each pixel value in the image array.
    """
    image = Image.open(image_path)
    image_array = np.array(image)
    print("Chose prefered operation")
    print("1. add")
    print("2. sub")
    print("3. mult")
    print("4. div")
    operation = input("Enter your choice (1 , 2 , 3 or 4): ")
    if operation == '1':
        add=int(input("enter the amount you want to add to each pixel value:"))
        answer = image_array + add
        answer_image=Image.fromarray(answer.astype('uint8'))
        
        answer_image.save(output_path)
        print(f"Operation done and saved to {output_path}")
    elif operation == '2':
        sub=int(input("enter the amount you want to subtract from each pixel value:"))
        answer = image_array - sub
        answer_image=Image.fromarray(answer.astype('uint8'))
        
        answer_image.save(output_path)
        print(f"Operation done and saved to {output_path}")
    elif operation == '3':
        mult=int(input("enter the amount you want to multiply each pixel value by:"))
        answer = image_array * mult
        answer_image=Image.fromarray(answer.astype('uint8'))
        
        answer_image.save(output_path)
        print(f"Operation done and saved to {output_path}")
    elif operation == '4':
        div=int(input("enter the amount you want to divide each pixel value by"))
        answer = image_array // div
        answer_image=Image.fromarray(answer.astype('uint8'))
        
        answer_image.save(output_path)
        print(f"Operation done and saved to {output_path}")

def encrypt_image(image_path, shift_value, output_path):
    """
    Encrypts the input image by adding a shift value to each pixel value and saves the encrypted image.
    """
    image = Image.open(image_path)
    image_array = np.array(image)
    encrypted_array = (image_array + shift_value) % 256  # Simple encryption by adding shift_value and modulo 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, shift_value, output_path):
    """
    Decrypts the input image by subtracting the shift value from each pixel value and saves the decrypted image.
    """
    image = Image.open(image_path)
    image_array = np.array(image)
    decrypted_array = (image_array - shift_value) % 256  # Decrypt by subtracting the same shift_value and modulo 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    print("3. Do mathemathical operations")
    print("4. swap pixles")
    choice = input("Enter your choice (1 , 2 , 3 or 4): ")

    if choice not in ['1', '2' , '3' , '4']:
        print("Invalid choice")
        return

    image_path = input("Enter the path of the image: ")
    shift_value = int(input("Enter the shift value: "))
    output_path = input("Enter the output path for the new image: ")

    if choice == '1':
        encrypt_image(image_path, shift_value, output_path)
    elif choice == '2':
        decrypt_image(image_path, shift_value, output_path)
    elif choice == '3':
        apply_operation(image_path, output_path)
    elif choice == '4':
        swap_pixel_values(image_path, output_path)
if __name__ == "__main__":
    main()