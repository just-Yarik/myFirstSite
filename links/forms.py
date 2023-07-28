from django import forms

class URLShortenForm(forms.Form):
    long_url = forms.URLField(label='Довге посилання', max_length=200)
