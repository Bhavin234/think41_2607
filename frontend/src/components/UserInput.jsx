import React from 'react';

const UserInput = ({ value, onChange, onSend }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    if (value.trim()) {
      onSend(value);
      onChange('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: '1rem' }}>
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Ask something..."
      />
      <button type="submit">Send</button>
    </form>
  );
};

export default UserInput;
