/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let n = 0
    return {
        increment: ()=> {
            n = n+1
            return init+n
        },
        decrement: () => {
            n = n - 1
            return init+n
        },
        reset: () => {
            n = 0
            return init+n
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */