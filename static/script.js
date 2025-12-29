function showTab(tab) {
  document.getElementById("visual").classList.add("hidden");
  document.getElementById("output").classList.add("hidden");
  document.getElementById(tab).classList.remove("hidden");
}

function runCode() {
  const code = document.getElementById("code").value;
  const language = document.getElementById("language").value;

  fetch("/run", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ code, language })
  })
  .then(res => res.json())
  .then(data => {

    if (data.type === "visualizer") {
      showTab("visual");

      let html = "";
      data.steps.forEach(s => {
        html += `
        <div class="bg-gray-800 border border-gray-700 p-4 rounded animate-slide">
          <div class="text-blue-400 font-semibold">Step ${s.step}</div>
          <div class="text-gray-300">Line: ${s.line}</div>
          <div class="text-yellow-400 text-sm">
            Variables: ${JSON.stringify(s.variables)}
          </div>
          <div class="text-green-400 text-sm">
            Output: ${s.output.join(", ")}
          </div>
        </div>`;
      });

      document.getElementById("visual").innerHTML = html;

    } else {
      showTab("output");
      document.getElementById("output").textContent = data.output;
    }
  });
}

