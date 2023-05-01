import "./App.css";
import ingredients_data from "./data/ingredients_data_g_per_ml.json";

function calculateVolume() {
  var ingrediense_value = document.getElementById("ingredienses").value;
  console.log("Button pressed:" + ingrediense_value);
}

function generateSelectItems() {
  const select = document.getElementById("ingredienses");
  for (let index = 0; index < ingredients_data.ingredients.length; index++) {
    const optionElement = document.createElement("option");
    optionElement.value = ingredients_data.ingredients[index].density;
    optionElement.textContent = ingredients_data.ingredients[index].name;
    select.appendChild(optionElement);
  }
}

generateSelectItems()

function App() {
  
  return (
    
    
    <div className="App">
      <header className="App-header"></header>
      <main>
        <form name="calculator_form">
          <select id="ingredienses" name="ingredienses">
          </select>
          <input type="text" placeholder="Antal gram"></input>
          <button type="button" onClick={calculateVolume}>
            submit
          </button>
        </form>
        <div className="result">Result</div>
      </main>
    </div>
  );
}

export default App;
