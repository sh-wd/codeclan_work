import logo from './moon.jpeg';
import './App.css';
import ArticlesContainer from './containers/ArticlesContainer';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <ArticlesContainer/>
      </header>
    </div>
  );
}

export default App;
