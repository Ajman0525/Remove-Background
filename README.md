This simple project uses the powerful `rembg` library in Python to automatically remove the background from an image, leaving the subject on a transparent layer.

### Prerequisites

Before running the script, you must have Python installed and the necessary libraries.

1.  **Install `rembg` and `Pillow`:**
    ```bash
    pip install rembg Pillow
    ```

### Usage

1.  **Save the Script:**
    Save your Python code as a file (e.g., `remove_bg.py`).

2.  **Prepare Your Image:**
    Place the image you want to process in the same directory as the script. **You must update the `input_image_path` variable in the Python file** to match the actual name of your input image (e.g., `'my_portrait.jpg'`).

    The default input/output paths are:
    ```python
    input_image_path = 'your_input_image.png' 
    output_image_path = 'your_output_image.png' 
    ```

3.  **Run the Script:**
    Execute the script from your terminal:
    ```bash
    python remove_bg.py
    ```
    *The model will automatically download the first time you run it.*
