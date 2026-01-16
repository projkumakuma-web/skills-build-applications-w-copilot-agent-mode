import React from 'react';
import logo from '../../../../../docs/octofitapp-small.png';

const OctofitLogo = ({ height = 48 }) => (
  <img src={logo} alt="OctoFit Logo" height={height} style={{ objectFit: 'contain', marginRight: 12 }} />
);

export default OctofitLogo;
