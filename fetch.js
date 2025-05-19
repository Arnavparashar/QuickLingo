async function translateText() {
  const textInput = document.getElementById("textInput").value.trim();
  const targetLang = document.getElementById("targetLang").value;
  const resultBox = document.getElementById("translatedText");
  const loadingIndicator = document.querySelector(".loading");

  // Reset and show loader
  resultBox.textContent = "";
  resultBox.style.color = "#e9d5ff";
  loadingIndicator.style.display = "flex";

  // Handle empty input
  if (!textInput) {
    loadingIndicator.style.display = "none";
    resultBox.textContent = "Please enter text to translate";
    resultBox.style.color = "#ef4444";
    return;
  }

  try {
    const response = await fetch("https://uie7qgzcgl.execute-api.us-east-1.amazonaws.com/Prod", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        text: textInput,
        target_language: targetLang
      })
    });

    const data = await response.json();
    loadingIndicator.style.display = "none";

    if (response.ok && data.translated_text) {
      resultBox.textContent = data.translated_text;
      resultBox.style.color = "#e9d5ff";
    } else {
      resultBox.textContent = data.error || "Translation failed.";
      resultBox.style.color = "#ef4444";
    }
  } catch (error) {
    loadingIndicator.style.display = "none";
    resultBox.textContent = "Network error. Please try again.";
    resultBox.style.color = "#ef4444";
    console.error("Fetch failed:", error);
  }
}
