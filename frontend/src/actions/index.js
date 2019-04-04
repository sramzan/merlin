let nextTodoId = 0;
export const addTodo = text => {
  nextTodoId += 1;
  return {
    id: nextTodoId,
    text,
    type: 'ADD_TODO',
  };
};

export const setVisibilityFilter = filter => ({
  filter,
  type: 'SET_VISIBILITY_FILTER',
});

export const toggleTodo = id => ({
  id,
  type: 'TOGGLE_TODO',
});

export const VisibilityFilters = {
  SHOW_ACTIVE: 'SHOW_ACTIVE',
  SHOW_ALL: 'SHOW_ALL',
  SHOW_COMPLETED: 'SHOW_COMPLETED',
};
