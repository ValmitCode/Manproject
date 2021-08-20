import React from 'react';
import './Header.css';
import { Link } from 'react-router-dom';

class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="header">
          <ul>
              <li><Link to="/">Devices</Link></li>
              <li><Link to="/create">Info</Link></li>
              <li><Link to="/login">Login</Link></li>
              <li><Link to="/reggistr">Register</Link></li>
              {/* <li><Link to="/github">GitHub</Link></li>
              <li><Link to="/help">Help</Link></li>
              <li className="right"><Link to="/tasks">Todo</Link></li> */}
          </ul>
      </div>
    );
  }
}

export default Header;
