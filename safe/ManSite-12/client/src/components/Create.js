import React from 'react';
import './Create.css';

class Create extends React.Component {
  constructor(props) {
    super(props);

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

    this.state = { 
        tasks: this.props.tasks,
        selectValue: 'none',
        inputValue: ""
    };
  }

  handleChange(event) {
      event.target.name === "select" ? this.setState({ selectValue: event.target.value }) : this.setState({ inputValue: event.target.value });
  }

  handleSubmit(event) {
    //   alert('submit');
      event.preventDefault();

      if (this.state.selectValue === 'none' || this.state.inputValue === '') {
        alert('Choose something!')
        return;
      }

      var send = { input: this.state.inputValue, select: this.state.selectValue };
      this.setState( {inputValue: '', selectValue: 'none' });

      fetch("http://localhost:19090/api/newTask", {
        method: "POST",
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            "Access-Control-Allow-Origin": "*"
        },
        body: JSON.stringify(send)
      }).then((result) => result.json()).then((info) => {console.log(info)});
      alert('Success!');
      console.log(JSON.stringify(send));
  }

  render() {
    return (
      <div className="create">
          <h2>Create task</h2>
          <form onSubmit={this.handleSubmit} method="POST" >
              <label>
                  Choose the task:
                  <select onChange={this.handleChange} name="select" value={this.state.selectValue}>
                    <option value="none">None</option>
                    {this.props.tasks.map((item) => {
                        return <option key={item.key} value={item.key}>{item.key}</option>
                    })}
                  </select>
              </label>
              <br />
                  <p>{ this.state.selectValue !== 'none' ? this.props.tasks[parseInt(this.state.selectValue) - 1].description : '' }</p>
              <label>
                Input data:
                <input onChange={this.handleChange} name="input" type="text" value={this.state.inputValue} />
              </label>
              <br />
              <input type="submit" value="Send" />
              
          </form>
      </div>
    );
  }
}

export default Create;
