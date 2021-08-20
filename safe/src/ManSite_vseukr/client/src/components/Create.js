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
      <div className='create'>
          <h1>Які параметри вимірює пристрій</h1>
          <p className="createText"><em>In all the premises, where people stay temporarily or permanently, carbon dioxide (CO2) is the main air pollutant. Normally, this gas is contained in the outdoor air at concentration of 300-400 ppm (0.03-0.04%), however, with each exhalation a person fills the surrounding air with a new portion of CO2 (18-25 liters per hour). Given that the concentration of carbon dioxide in the exhaled air is 100 times higher than in clean air, a room quickly becomes potentially dangerous to health.
Increasing level of CO2 can cause symptoms of lack of oxygen, deterioration of cognitive abilities, directly affect one’s ability to work, lead to its complete loss, which ultimately affects the educational process in schools and the results of companies.
One should take into account many products that emit volatile organic compounds into the air. The concentration of these substances indoors can be even 100 times higher than outside.
Volatile organic compounds or VOCs are chemicals that are released in the form of gases from solids or liquids, easily evaporate into the air, even at room temperature. Of course, formaldehyde, benzene and phenol are among the most dangerous according to the classification of the US Environmental Protection Agency (EPA), US Green Building Council (USGBC) and European Union (EU).
Studies claim that values above 500 ng/l (nanograms per liter) of volatile organic compounds can pose a health hazard to homeowners. However, data from thousands of tested houses show that average value is 1200 ng/l - more than twice the allowable level [3]. Even moderately elevated levels of these chemicals in the air can cause health problems for people, especially those suffering from allergies and asthma.
Because of this monitoring of air composition to preserve health and life, which becomes possible and convenient thanks to the developed system of air quality monitoring in any place chosen by the user, with the ability to obtain data on the result directly by the user, becomes especially relevant.
      </em></p></div>
    );
  }
}

export default Create;
