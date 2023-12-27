#### Install Package

```bash
pip install weapp_builder
```


### Example Usage

```python
# Importing the CodeGenerator and ImageProcessor classes
from weapp_builder.utilities import CodeGenerator, ImageProcessor

# Create instances of the classes
code_generator = CodeGenerator()
image_processor = ImageProcessor()

# Example usage of CodeGenerator
code_text = "Your image description text here"
generated_code = code_generator.generate_code(code_text)
print(generated_code)

# Example usage of ImageProcessor
image_path = "path/to/your/image.jpg"
api_key = "your_openai_api_key"  # Provide your OpenAI API key
image_description = image_processor.get_image_description(image_path, api_key)
print(image_description)
```

For running the Streamlit app, you can create a separate Python script (let's call it `app_runner.py`) with the following content:

```python
# app_runner.py
from weapp_builder import main

if __name__ == "__main__":
    main()
```

Then, you can run this script to launch the Streamlit app:

```bash
streamlit run app_runner.py
```


Ensure you have your OpenAI API key configured in your environment variables or pass it directly when calling methods that require it.