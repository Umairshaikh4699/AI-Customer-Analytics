const API = "http://localhost:5000";

function addCustomer() {
  const nameInput = document.getElementById("name");
  const name = nameInput.value.trim();

  if (!name) {
    alert("Please enter a name");
    return;
  }

  fetch(API + "/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name })
  }).then(() => {
    nameInput.value = "";
    loadCustomers();
  });
}

function loadCustomers() {
  fetch(API + "/customers")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("list");
      list.innerHTML = "";
      data.forEach(c => {
        const li = document.createElement("li");
        li.textContent = c.name;
        list.appendChild(li);
      });
    });
}

loadCustomers();
