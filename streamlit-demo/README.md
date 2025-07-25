Streamlit makes it super easy to build interactive web apps in pure Python. Here's a step-by-step guide to creating your first basic Streamlit app.

## 1. **Install Streamlit**

If you haven't already, install Streamlit using pip:

```bash
pip install streamlit
```

## 2. **Create a Python Script**

Create a new file called `app.py` (or any name you like).

## 3. **Write Your First Streamlit App**

Open `app.py` and add the following code:

```python
import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit web app.")

# Add a simple interactive widget
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")
```

### Explanation:
- `st.title()` adds a big title.
- `st.write()` can display text, data, and more.
- `st.text_input()` creates a text box for user input.
- The app greets the user by name if they enter one.

## 4. **Run the App**

In your terminal, run:

```bash
streamlit run app.py
```

This will open your app in a new browser window at `http://localhost:8501`.

## 5. **Next Steps**

- Try adding other widgets like `st.button()`, `st.slider()`, or `st.selectbox()`.
- Explore [Streamlit documentation](https://docs.streamlit.io/) for more features.

**That's it!** You've built a basic interactive web app with Streamlit.

&mdash; *gpt-4.1*

<br>
