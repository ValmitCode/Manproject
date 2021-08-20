import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';

import './Card.css';

class Login extends React.Component {

  render(){
      return(
    <div className='container'>
    <div className='card'>
      <h1>Please Log In</h1>
      <form>
        <label>
          <p>Username</p>
          <input type="text"/>
        </label>
        <label>
          <p>Password</p>
          <input type="password"/>
        </label>
        <div className='settin'>
        <Link to={{pathname: `/`, name: "fd"}}>Log in</Link>
        </div>
      </form>
    </div>
    </div>
      );
  }
}
export default Login;