import React from 'react';
import Card from './Card';
// import './Card.css';
import './Body.css';

class Body extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="body">
          <ul style={{}}>
            {this.props.tasks.map(function(item) {
                return <Card key={item.key} name={item.key} title={item.title} short_description={item.short_description} />
            })}
          </ul>
      </div>
    );
  }
}

export default Body;
