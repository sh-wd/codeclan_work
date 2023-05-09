import './App.css';
import ArticlesContainer from './containers/ArticlesContainer';

function App() {

  const sources = [
    {name: "Latest", url: "https://api.spaceflightnewsapi.net/v4/articles/?format=json&limit=21"},
    {name: "Nasa", url: "https://api.spaceflightnewsapi.net/v4/articles/?format=json&news_site=NASA&limit=21"},
    {name: "SpaceNews", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=SpaceNews&limit=21"},
    {name: "Arstechnica", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=Arstechnica&limit=21"},
    {name: "The Launch Pad", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=The%20Launch%20Pad&limit=21"},
    {name: "CNBC", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=CNBC&limit=21"},
    {name: "Teslarati", url: "https://api.spaceflightnewsapi.net/v4/articles/?news_site=Teslarati&limit=21"},
  ]

  return (
    <div className="App">
      <header className="App-header">
        <ArticlesContainer sources={sources}/>
      </header>
    </div>
  );
}

export default App;
