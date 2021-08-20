import React from 'react';
import {Link} from 'react-router-dom';
import './Card.css';
// import '../index.css';

class Card extends React.Component {
    constructor(props) {
      super(props);
      this.state = {};
    }
  
    render() {

        const ColoredLine = ({ color }) => (
            <hr
                style={{
                    color: color,
                    backgroundColor: color,
                    height: 1,
                    borderStyle: "solid"
                }}
            />
        );

        return (
            <li className='container'>
                <div className='card'>
                    <div className='circle'>
                        <h2>{this.props.title}</h2>
                        <ColoredLine color="#dddddd" />
                    </div>
                    <div className='content'>
                        <p>{this.props.short_description}</p>
                        <ColoredLine color="#dddddd" />
                        <Link to={{pathname: `/create`, name: this.props.name}}>More statistics {this.props.name}</Link>
                    </div>
                    <div className='settin'>
                    <Link to={{pathname: `/sett`, name: this.props.name}}>Settings {this.props.name}</Link>
                    </div>
                </div>
            </li>
        );
    }
}

  export default Card;