import React, { useState } from 'react';
import '../../styles/infoCuenta.css';

const InfoCuenta = ({ name, phone, address, setName, setPhone, setAddress, onSave }) => {
  return (
    <div className="info-basic">
      <h3>Información básica</h3>

      <div className="info-field">
        <label>Nombre(s):</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </div>

      <div className="info-field">
        <label>Teléfono:</label>
        <input
          type="text"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
      </div>

      <div className="info-field">
        <label>Dirección:</label>
        <input
          type="text"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
        />
      </div>

      <button className="save-button" onClick={onSave}>Guardar datos</button>
    </div>
  );
};

export default InfoCuenta;
