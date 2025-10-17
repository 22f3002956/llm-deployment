document.getElementById("generate").addEventListener("click", async () => {
    const brief = document.getElementById("brief").value.trim();
    const project = document.getElementById("project-name").value.trim() || "myapp";
    const loader = document.getElementById("loader");
    const consoleBox = document.getElementById("console");
    const resultLink = document.getElementById("result-link");
  
    if (!brief) {
      consoleBox.textContent = "⚠️ Please enter a brief first.";
      return;
    }
  
    loader.classList.remove("hidden");
    consoleBox.textContent = "🧠 Sending request to AI model...\n";
    resultLink.textContent = "";
  
    try {
      const res = await fetch("/api-endpoint", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          secret: "mysecret123",
          brief: brief,
          project_name: project
        })
      });
  
      const data = await res.json();
      loader.classList.add("hidden");
  
      if (data.status === "success") {
        consoleBox.textContent += `✅ ${data.message}\n`;
        consoleBox.textContent += `🌐 URL: ${data.project_url}\n`;
        resultLink.href = data.project_url;
        resultLink.textContent = "View Live App →";
      } else {
        consoleBox.textContent += "❌ Error: " + (data.error || "Unknown issue.") + "\n";
      }
    } catch (err) {
      loader.classList.add("hidden");
      consoleBox.textContent += "⚠️ Network or server error.\n";
      console.error(err);
    }
  });
  