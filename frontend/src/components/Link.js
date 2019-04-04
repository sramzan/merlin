import React from 'react';
import { Button } from '@material-ui/core';
import PropTypes from 'prop-types';

const Link = ({ active, children, onClick }) => (
  <Button
    disabled={active}
    onClick={onClick}
    style={{
      marginLeft: '4px',
    }}
  >
    {children}
  </Button>
);

Link.propTypes = {
  active: PropTypes.bool.isRequired,
  children: PropTypes.node.isRequired,
  onClick: PropTypes.func.isRequired,
};

export default Link;
