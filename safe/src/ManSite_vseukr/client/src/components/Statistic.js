import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

import './Card.css';

class Statistic extends React.Component {

  render(){
      return(
    <div className='container'>
    <div className='card'>
      <h1>Statistic from device1:</h1>
        <p className="text">Min VOC for 7 days: 2 ppb</p>
        <p className="text">Max VOC for 7 days: 37 ppb</p>
        <p className="text">Mean VOC for 7 days: 4 ppb</p>
        <p className="text">Min CO2 for 7 days: 326 ppm</p>
        <p className="text">Max CO2 for 7 days: 1073 ppm</p>
        <p className="text">Mean CO2 for 7 days: 538 ppm</p>
        <p className="text">Min temperature for 7 days: 21 ℃</p>
        <p className="text">Max temperature for 7 days: 27 ℃</p>
        <p className="text">Mean temperature for 7 days: 24 ℃</p>

    </div>
    </div>
      );
  }
}
export default Statistic;