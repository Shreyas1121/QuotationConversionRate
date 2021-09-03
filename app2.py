#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%%writefile app.py
 
import pickle
import streamlit as st
import base64

 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Sales_Quotation, Expiring_Quotations, Product_ID, Inquiry_Channel):   
 
    # Pre-processing user input    
    if Product_ID == "MetalProduct1":
        Product_ID_MetalProduct1 = 1
        Product_ID_MetalProduct2 = 0
        Product_ID_MetalProduct3 = 0
    else:
        if Product_ID == "MetalProduct2":
            Product_ID_MetalProduct1 = 0
            Product_ID_MetalProduct2 = 1
            Product_ID_MetalProduct3 = 0
        else:
            if Product_ID == "MetalProduct3":
                Product_ID_MetalProduct1 = 0
                Product_ID_MetalProduct2 = 0
                Product_ID_MetalProduct3 = 1
            
 
    if Inquiry_Channel == "Email":
        Inquiry_Channel_Email = 1
        Inquiry_Channel_InternalTeam = 0
    else:
        Inquiry_Channel_InternalTeam = 1
        Inquiry_Channel_Email = 0
 
 
 
#    LoanAmount = LoanAmount / 1000
 
    # Making predictions 
    predictions = classifier.predict( 
        [[Sales_Quotation, Expiring_Quotations, Product_ID_MetalProduct1, Product_ID_MetalProduct2, Product_ID_MetalProduct3,Inquiry_Channel_Email,Inquiry_Channel_InternalTeam]])
     

    return predictions
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:red;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Sales Quotation Conversion Rates</h1>

    </div> 
    """
    LOGO_IMAGE = "logo.png"

    st.markdown(
        """
        <style>
        .container {
            display: flex;
        }
        .logo-text {
            font-weight:700 !important;
            font-size:50px !important;
            color: #f9a01b !important;
            padding-top: 75px !important;
        }
        .logo-img {
            float: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="container">
            <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}" align = "right">

        </div>
        """,
        unsafe_allow_html=True
    )      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    


      
    # following lines create boxes in which user can enter data required to make prediction 
    #Gender = st.selectbox('Gender',("Male","Female"))
    Sales_Quotation = st.number_input("Total Sales Quotation")
    Expiring_Quotations = st.number_input("Expiring Quotations")
    Product_ID = st.selectbox('Product ID',("MetalProduct1", "MetalProduct2", "MetalProduct3")) 
    #ApplicantIncome = st.number_input("Applicants monthly income") 
    #LoanAmount = st.number_input("Total loan amount")
    Inquiry_Channel = st.selectbox('Inquiry Channel',("Email","Inquiry Channel_Internal Sales Lead-PersonA"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Sales_Quotation, Expiring_Quotations, Product_ID, Inquiry_Channel) 
        st.success('Your Predicted Sales Quotation Conversion Rate is {} %'.format(result))
        #print(LoanAmount)
     
if __name__=='__main__': 
    main()

