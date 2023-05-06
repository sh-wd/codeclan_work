import logo from './moon.png';
import './App.css';
import ArticlesContainer from './containers/ArticlesContainer';

function App() {

  const sources = [
    {name: "Latest", url: "https://api.spaceflightnewsapi.net/v4/articles/?format=json&limit=20"},
    {name: "Nasa", url: "https://api.spaceflightnewsapi.net/v4/articles/?format=json&news_site=NASA"},
    {name: "SpaceNews", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=SpaceNews"},
    {name: "Arstechnica", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=Arstechnica"},
    {name: "The Launch Pad", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=The%20Launch%20Pad"},
    {name: "CNBC", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=CNBC"},
    {name: "Teslarati", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=Teslarati"},
  ]

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo of the moon" />
        <ArticlesContainer sources={sources}/>
      </header>
    </div>
  );
}

export default App;
