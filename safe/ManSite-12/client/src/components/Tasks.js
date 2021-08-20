import React from 'react';
import './Tasks.css';
import { Link } from 'react-router-dom';
// import { response } from 'express';

class Tasks extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        tasks: {}
    };
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
      fetch('http://localhost:19090/api/tasks', {
          "method": "GET"
      })
        .then((response) => response.json())
        .then((response) => {this.setState({tasks: response})})
        .catch(err => {console.log(err)})
  }

  handleClick(e) {
    e.preventDefault();
    // const trs = JSON.stringify(this.state.tasks);
    console.log(this.state.tasks.tasks);
  }

  render() {
    const tasks = this.state.tasks.tasks;
    console.log(tasks);
    return (
      <div className="tasks">
          <h2>Todo List:</h2>
          <ul>
            {tasks === undefined ? "Wait" : tasks.map(item => {
                return <li key={item.id} >
                  input: {item.input}
                  <br />
                  select: {item.select}
                  <br />
                  <Link to={'/tasks/' + item.id} >Solution</Link>
                </li>
            })}
            {/* <input type="submit" onClick={this.handleClick} value="Send" /> */}
          </ul>
      </div>
    );
  }
}

export default Tasks;
