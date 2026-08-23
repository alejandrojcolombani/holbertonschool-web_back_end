export default function appendToEachArrayValue(array, appendString) {
  for (const [index, value] of array.entries()) {
    array.splice(index, 1, `${appendString}${value}`);
  }
  return array;
}
