import React, { useState } from 'react';
import "../../styles/Seguridad.css";
import { useContext } from 'react';
import { Context } from "../store/appContext"; // Ajusta la ruta según tu configuración

const Seguridad = () => {
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errors, setErrors] = useState({
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
  });
  const { actions } = useContext(Context);

  const validate = () => {
    let valid = true;
    const newErrors = {};

    if (!currentPassword.trim()) {
      newErrors.currentPassword = 'Requiere valor el campo';
      valid = false;
    }
    if (!newPassword.trim()) {
      newErrors.newPassword = 'Requiere valor el campo';
      valid = false;
    }
    if (!confirmPassword.trim()) {
      newErrors.confirmPassword = 'Requiere valor el campo';
      valid = false;
    } else if (newPassword !== confirmPassword) {
      newErrors.confirmPassword = 'El campo nueva contraseña y confirmar nueva contraseña deben coincidir.';
      valid = false;
    }

    setErrors(newErrors);
    return valid;
  };

  const handlePasswordChange = async () => {
    if (!validate()) {
      return;
    }
    try {
      const response = await fetch(`${process.env.BACKEND_URL}/api/change-password`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sessionStorage.getItem('access_token')}`
        },
        body: JSON.stringify({
          currentPassword,
          newPassword,
          confirmPassword
        })
      });

      const data = await response.json();

      if (response.ok) {
        alert('Contraseña actualizada exitosamente');
      } else {
        alert(`Error: ${data.msg}`);
      }
    } catch (error) {
      console.error('Error al cambiar la contraseña:', error);
      alert('Error al cambiar la contraseña. Inténtalo de nuevo más tarde.');
    }
  };

  return (
    <div className="security-form">
      <h2 className="security-title">Cambiar contraseña</h2>
      <div className="form-group">
        <label htmlFor="currentPassword">Contraseña actual</label>
        <input
          type="password"
          id="currentPassword"
          className={`form-control ${errors.currentPassword ? 'error' : ''}`}
          value={currentPassword}
          onChange={(e) => setCurrentPassword(e.target.value)}
        />
        {errors.currentPassword && <p className="error-message">{errors.currentPassword}</p>}
      </div>
      <div className="form-group">
        <label htmlFor="newPassword">Nueva contraseña</label>
        <input
          type="password"
          id="newPassword"
          className={`form-control ${errors.newPassword ? 'error' : ''}`}
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
        />
        {errors.newPassword && <p className="error-message">{errors.newPassword}</p>}
      </div>
      <div className="form-group">
        <label htmlFor="confirmPassword">Confirmar nueva contraseña</label>
        <input
          type="password"
          id="confirmPassword"
          className={`form-control ${errors.confirmPassword ? 'error' : ''}`}
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
        {errors.confirmPassword && <p className="error-message">{errors.confirmPassword}</p>}
      </div>
      <button
        className="btn"
        onClick={handlePasswordChange}
      >
        Guardar
      </button>
    </div>
  );
};

export default Seguridad;
