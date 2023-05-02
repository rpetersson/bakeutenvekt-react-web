import "./App.css";
import ingredients_data from "./data/ingredients_data_g_per_ml.json";
import React from "react";

function omvandlare(volumeInDl) {
  let hela = Math.trunc(volumeInDl);
  let omv = volumeInDl - hela;
  let msk = omv / 0.15;
  msk = Math.round(msk);
  var mskDiv = document.getElementById("msk")
  mskDiv.textContent = `${msk} tbsp`
  var resultDiv = document.getElementById("result")
  resultDiv.textContent = `${hela} dl +`
}


function calculateVolume() {
  // volume (in dl) = mass (in g) / density (in g/ml) / 100
  var ingrediense_value = document.getElementById("ingredientSelect").value;
  var form_gram = document.getElementById("form_gram").value
  var volumeInDl =  (form_gram / ingrediense_value) / 100
  var resultDiv = document.getElementById("result")
  //resultDiv.textContent = `${volumeInDl} dl`
  omvandlare(volumeInDl)
}


function App() {
  const [selectedIngredient, setSelectedIngredient] = React.useState("");

  // Create an array of <option> elements based on the data
  const ingredientOptions = ingredients_data.ingredients.map((ingredient) => (
    <option key={ingredient.name} value={ingredient.density}>
      {ingredient.name}
    </option>
  ));

  function handleIngredientChange(event) {
    calculateVolume()
    setSelectedIngredient(event.target.value);
  }

  return (
    <div className="App">
      <header className="App-header"></header>
      <main>
        <form name="calculator_form">
        <input type="text" placeholder="Grams" id='form_gram' onChange={handleIngredientChange}></input>
          <select
            id="ingredientSelect"
            value={selectedIngredient}
            onChange={handleIngredientChange}
          >
            
            <option value="">Select an ingredient</option>
            {ingredientOptions}
          </select>
          
        </form>
        <div id="result">0</div>
        <div id="msk">0</div>
      </main>
    </div>
  );
}

export default App;
