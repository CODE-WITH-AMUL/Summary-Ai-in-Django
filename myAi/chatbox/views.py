from django.shortcuts import render
from transformers import pipeline

# Load the summarizer model once
summarizer = pipeline("summarization")

def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if len(text.split()) > 50:  # Ensure text is long enough to summarize
            summary = summarizer(text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']
        else:
            summary = "Please enter a longer text for summarization."
        return render(request, "index.html", {"summary": summary, "text": text})
    return render(request, "index.html")
