import React from 'react';
import './Solution.css';

class Solution extends React.Component {
  constructor(props) {
    super(props);
    this.state = { tasks: [], result: "Wait" };

    this.findTaskById = this.findTaskById.bind(this);

    console.log(this.props.match.params.id);
  }

  componentDidMount() {
    fetch('http://localhost:19090/api/tasks', {
        "method": "GET"
    })
      .then((response) => response.json())
      // .then((response) => {this.setState({tasks: response})})
      .then((response) => {this.findTaskById(response.tasks, this.props.match.params.id)})
      .catch(err => {console.log(err)})
}

  findTaskById(arr, id) {
    var task;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].id === id) {
        this.setState({ result: arr[i].result });
      }
    }
  }

  render() {
    return (
      <div className="solution">
          <h2>Solution: {this.props.match.params.id}</h2>
          <h3>Result: {this.state.result}</h3>
      </div>
    );
  }
}

export default Solution;
