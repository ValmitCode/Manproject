import React from 'react';
// import logo from './logo.svg';
// import './App.css';
import Header from './components/Header';
import Body from './components/Body';
import Bottom from './components/Bottom';
import { Route, Switch } from 'react-router-dom';
import Create from './components/Create';
import Tasks from './components/Tasks';
import Solution from './components/Solution';
import Settings from './components/Settings';
import Login from './components/Login';
import Register from './components/Register';
import Statistic from './components/Statistic';


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      tasks: [
        {
            title: "device 1",
            short_description: "CO2: 1056; VOC: 16; temperature: 22 ℃",
            description: "Long description1",
            key: ""
        },
        {
            title: "device 2",
            short_description: "CO2: 753 ppm; VOC: 2 ppb; temperature: 24 ℃",
            description: "Long description2",
            key: ""
        },
        {
            title: "device 3",
            short_description: "CO2: 342; VOC: 32;",
            description: "Long description3",
            key: ""
        },
        {
          title: "device 4",
          short_description: "CO2: 1433; VOC: 4;",
          description: "Long description4",
          key: ""
      }
      ] 
    }
  }

  render() {
    return (
      <>
        <Header />
        <Switch>
          <Route exact path="/create" render={() => <Create tasks={this.state.tasks} name={'none'} />} />
          {/* <Route path="/create/:name" render={() => <Create tasks={this.state.tasks} />} /> */}
          <Route exact path="/" render={() => <Body tasks={this.state.tasks} />} />
          <Route exact path="/tasks" render={() => <Tasks />} />
          <Route exact path="/login" render={() => <Login/>} />
          <Route exact path="/sett" render={() => <Settings/>} />
          <Route exact path="/reggistr" render={() => <Register/>} />
          <Route exact path="/stat" render={() => <Statistic/>} />
          <Route path="/tasks/:id" component={Solution} />
        </Switch>
        <Bottom />
      </>
    );
  }
}

export default App;
