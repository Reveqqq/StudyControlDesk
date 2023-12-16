// var lesson_id = null;

// test.js
import { reactive } from "vue"

export const lesson_id = reactive({
  id: 0,   // <-- make reactive in template
});

export const ChangeId = (id) => {
  lesson_id.id = id;
};
