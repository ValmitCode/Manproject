import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

import './Card.css';

class Settings extends React.Component {

  render(){
      return(
        <div className='container'>
        <div className='card'>
          <h1>Settings</h1>
          <form>
            <label>
              <p>Interval for collecting statistics (min)</p>
              <input type="text"/>
            </label>
            <label>
              <p>Data refresh rate from server to user (min)</p>
              <input type="text"/>
            </label>
            <label>
              <p>Data refresh rate from device to server (min)</p>
              <input type="text"/>
            </label>
            <div className='settin'>
            <Link to={{pathname: `/`, name: "fd1"}}>Apply</Link>
            </div>
            <div className='settin2'>
            <Link to={{pathname: `/`, name: "fd2"}}>Shutdown device1</Link>
            </div>
            <div className='settin3'>
            <Link to={{pathname: `/`, name: "fd3"}}>Reboot device1</Link>
            </div>
          </form>
        </div>
        </div>
      );
  }
}
export default Settings;