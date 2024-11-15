import streamlit as st
import lamini
import os

os.environ["LAMINI_API_KEY"] = "6406b21a12ee13fd7d91e596e37446c524c0601598513d6a259ba516064afb66"

# Initialize Lamini model
llm = lamini.Lamini("meta-llama/Llama-3.2-3B-Instruct")
lamini.api_key = "6406b21a12ee13fd7d91e596e37446c524c0601598513d6a259ba516064afb66"


# Input for generating text
st.header("Generate Text")
prompt = st.text_area("Enter a prompt:", value="What are the benefits of route optimization in logistics?")
if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        response = llm.generate(prompt)
        st.success("Response generated!")
        st.markdown(response)

# Section for fine-tuning
# st.header("Fine-Tune the Model")
# st.markdown("Provide training data to fine-tune the model.")
# with st.expander("Enter Training Data"):
#     col1, col2 = st.columns(2)
#     inputs = col1.text_area("Input Texts (comma-separated):", value="What is route optimization?, How can logistics reduce costs?")
#     outputs = col2.text_area("Output Texts (comma-separated):", value="It improves efficiency., By optimizing delivery routes.")

# if st.button("Fine-Tune Model"):
#     input_list = [text.strip() for text in inputs.split(",")]
#     output_list = [text.strip() for text in outputs.split(",")]
#     if len(input_list) != len(output_list):
#         st.error("The number of inputs must match the number of outputs!")
#     else:
#         training_data = [{"input": inp, "output": out} for inp, out in zip(input_list, output_list)]
#         with st.spinner("Fine-tuning the model..."):
#             llm.tune(data_or_dataset_id=training_data)
#             st.success("Fine-tuning job started! Check your Lamini dashboard for status.")

# Footer
# st.markdown("---")
# st.caption("Built with [Lamini](https://lamini.ai) and [Streamlit](https://streamlit.io)")
