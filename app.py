import streamlit as st
import pandas as pd
import subprocess
import os

# Set Page Layout and Title
st.set_page_config(layout="centered", page_title="Automated Data Extraction", page_icon="🔍")
st.title("🔍 Automated Data Extraction App")
st.write("Run a script to extract data and display the results from CSV files.")

# URL Input Section
st.sidebar.header("Settings")
URL = st.sidebar.text_input("🔗 Enter URL to process:")
run_script = st.sidebar.button("🚀 Run Data Extraction")

# Progress Bar
progress_bar = st.progress(0)

# Running the Script with Step-by-Step Feedback
if URL and run_script:
    with st.spinner("Running the data extraction script..."):
        # Step 1: Run the scraper.py script
        st.subheader("Script Output")
        progress_bar.progress(20)
        
        try:
            # Run scraper.py and capture the output
            result = subprocess.run(["python", "scraper.py"], check=True, capture_output=True, text=True)
            st.success("✅ Script executed successfully!")
            st.code(result.stdout, language='python')
            progress_bar.progress(60)
        
        except subprocess.CalledProcessError as e:
            st.error("❌ Error running scraper.py:")
            st.code(e.stderr, language='text')
            st.stop()
    
    # Step 2: Display CSV Data as DataFrames
    csv_files = ["categories_and_links.csv", "page_details.csv"]  # replace with actual CSV file names
    progress_step = int(40 / len(csv_files))  # Calculate progress step for each file
    progress = 60  # Start progress at 60 after running the script

    for csv_file in csv_files:
        if os.path.exists(csv_file):
            st.write(f"### 📄 Contents of `{csv_file}`:")
            df = pd.read_csv(csv_file)
            
            # Enhance Data Display with Additional Information
            st.dataframe(df)
            st.write(f"Data from `{csv_file}`:")
            st.write(f"- Rows: {len(df)}")
            st.write(f"- Columns: {list(df.columns)}")
            
            progress += progress_step
            progress_bar.progress(progress)
        else:
            st.warning(f"`{csv_file}` not found.")
    
    progress_bar.progress(100)
    st.success("🎉 Data display complete!")

else:
    st.info("🔹 Please enter a URL in the sidebar and click 'Run Data Extraction'.")

# Display Tips and Instructions at the Bottom
st.markdown("""
---
### 🛠️ Tips:
1. Please enter the URL in the sidebar as: https://www.yellowpages.com/
2. Ensure that the URL is correct before running.
3. Check the script output for any error messages if the script fails to run.
4. Missing files will show a warning message.
""")
