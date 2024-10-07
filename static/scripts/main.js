async function getTropicalPlants() {
  return fetch("/tropical-plant-json").then((response) => response.json());
}

async function refreshTropicalPlants() {
  document.getElementById("tropical_plants_cards").innerHTML = "";
  document.getElementById("tropical_plants_cards").className = "";
  const tropicalPlants = await getTropicalPlants();
  let htmlString = "";
  let classNameString = "";

  if (tropicalPlants.length === 0) {
    classNameString =
      "flex flex-col items-center justify-center min-h-[24rem] p-6";
    htmlString = `<p class="text-center">There are no plants in the shop just yet. 🌱</p>`;
  } else {
    htmlString += `
          <h2 class="text-3xl font-bold tracking-tighter text-green-800 sm:text-5xl text-center my-8">Our best sellers!</h2>
          <div class="grid gap-6 sm:grid-cols-2 xl:grid-cols-4 p-3 md:p-10">
    `;
    tropicalPlants.forEach((item) => {
      htmlString += `
            <div class="relative group">
                <div class="flex flex-col items-center justify-between group rounded-md shadow-lg transition-transform group-hover:scale-105 overflow-hidden">
                    <img src="/static/image/plant_placeholder.png"
                         alt="Plant placeholder"
                         class="w-auto h-60 p-2" />
                    <div class="bg-white p-4 flex flex-col gap-2 w-full">
                        <div class="flex flex-col">
                            <h3 class="font-semibold text-lg text-green-800 tracking-wide">${item.fields.name}</h3>
                            <p class="text-green-600">${item.fields.price}, ${item.fields.weight} lbs</p>
                        </div>
                        <p class="text-green-600">${item.fields.description}</p>
                    </div>
                </div>
                <div class="absolute -top-2 right-2 md:-right-4 flex space-x-1 group-hover:scale-105 transition-transform">
                    <a href="/edit-tropical-plant/${item.pk}"
                       class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                        <svg xmlns="http://www.w3.org/2000/svg"
                             class="h-6 w-6 sm:h-8 sm:w-8"
                             viewBox="0 0 20 20"
                             fill="currentColor">
                            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                        </svg>
                    </a>
                    <a href="/delete-tropical-plant/${item.pk}"
                       class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                        <svg xmlns="http://www.w3.org/2000/svg"
                             class="h-6 w-6 sm:h-8 sm:w-8"
                             viewBox="0 0 20 20"
                             fill="currentColor">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                        </svg>
                    </a>
                </div>
            </div>
            `;
    });
    htmlString += "</div>";
  }
  document.getElementById("tropical_plants_cards").className = classNameString;
  document.getElementById("tropical_plants_cards").innerHTML = htmlString;
}

refreshTropicalPlants();

const modal = document.getElementById("crudModal");
const modalContent = document.getElementById("crudModalContent");

function showModal() {
  const modal = document.getElementById("crudModal");
  const modalContent = document.getElementById("crudModalContent");

  modal.classList.remove("hidden");
  setTimeout(() => {
    modalContent.classList.remove("opacity-0", "scale-95");
    modalContent.classList.add("opacity-100", "scale-100");
  }, 50);
}

function hideModal() {
  const modal = document.getElementById("crudModal");
  const modalContent = document.getElementById("crudModalContent");

  modalContent.classList.remove("opacity-100", "scale-100");
  modalContent.classList.add("opacity-0", "scale-95");

  setTimeout(() => {
    modal.classList.add("hidden");
  }, 150);
}

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalBtn").addEventListener("click", hideModal);

function addTropicalPlant() {
  fetch("/add-tropical-plant-ajax/", {
    method: "POST",
    body: new FormData(document.querySelector("#addTropicalPlantForm")),
  }).then((response) => refreshTropicalPlants());

  document.getElementById("addTropicalPlantForm").reset();
  document.querySelector("[data-modal-toggle='crudModal']").click();

  return false;
}

document
  .getElementById("addTropicalPlantForm")
  .addEventListener("submit", (e) => {
    e.preventDefault();
    addTropicalPlant();
  });
