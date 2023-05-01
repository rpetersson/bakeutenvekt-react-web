import logo from './logo.svg';
import './App.css';

function calculateVolume() {
  var ingrediense_value = document.getElementById("ingredienses").value
  console.log("Button pressed:" + ingrediense_value)
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
      </header>
      <main>
        <form name='calculator_form'>
          <select id="ingredienses" name="ingredienses">
            <option value="2">mel</option>
            <option value="3">korn</option>
            <option value="4">sylt</option>
            <option value="5">sirup</option>
          </select>
          <input type='text' placeholder='Antal gram'></input>
          <button type='button' onClick={calculateVolume}>submit</button> 
        </form>
        <div className='result'>Result</div>
      </main>

    </div>
  );
}



export default App;
