{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c49d799c-e2eb-4977-b07b-e62179f55697",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import streamlit as st\n",
    "user_input = st.text_area(\"Enter Your Email ID\")\n",
    "\n",
    "pattern = re.compile(r'([A-Za-z0-9]+[.])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')\n",
    "\n",
    "def check(email):\n",
    "    if re.fullmatch(pattern, email):\n",
    "      return \"Valid email id\"\n",
    "    else:\n",
    "      return \"Invalid email id\"\n",
    "      \n",
    "if(st.button('Check')):\n",
    "    response = check(user_input)\n",
    "    st.success(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71833f1b-eb34-4a0a-85e7-1d6e28a48fd5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
