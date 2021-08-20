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



class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { 
      tasks: [
        {
            title: "device 1",
            short_description: "CO2: 1056; VOC: 16; temperature: 22℃",
            description: "Long description1",
            key: ""
        },
        {
          title: "device 2",
          short_description: "CO2: 957; VOC: 13; temperature: 24℃",
          description: "Long description1",
          key: ""
        },
        {
            title: "TTL3",
            short_description: "Short description3 Quisque congue nulla eget pulvinar maximus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut sagittis justo sit amet pretium mollis. Mauris dignissim dignissim magna id volutpat. Ut tristique cursus velit, id varius nibh rhoncus vel. Sed vitae enim sit amet metus congue iaculis. Etiam pharetra, urna eget eleifend congue, elit quam congue erat, suscipit commodo dolor massa lobortis felis. Curabitur quis sapien suscipit, elementum velit at, dictum nisi. Vestibulum convallis massa diam, non sagittis ex luctus eget. Nullam non orci non ante tincidunt porttitor nec ut odio. ",
            description: "Long description3",
            key: "3"
        },
        {
          title: "TTL4",
          short_description: "Short description4 Donec mattis diam enim, id suscipit lectus semper vitae. Cras ornare, magna eu hendrerit hendrerit, metus lectus aliquam massa, vel ullamcorper ex odio sit amet velit. Proin condimentum molestie ante, eget dapibus leo euismod eu. Etiam commodo diam neque, sit amet accumsan enim tincidunt et. Pellentesque vitae volutpat massa. Ut vel convallis quam, eget vestibulum diam. Sed mattis dui quis commodo efficitur. Donec non porta lacus, id fermentum erat. Sed egestas erat ut leo vestibulum pulvinar. ",
          description: "Long description4",
          key: "4"
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
          <Route path="/tasks/:id" component={Solution} />
        </Switch>
        <Bottom />
      </>
    );
  }
}

export default App;
