export default class WheelOfFortune {
  constructor(element, labels) {
    this.animationSpins = 5;
    this.animationTime = 5000;
    this.element = element;
    this.labels = labels;
    this.container = create("div", "wheel-of-fortune__container");
    this.element.appendChild(this.container);
    this.degreeses = 360 / labels.length;
    this.current = 0;
    this.isLock = false;

    this.labels.forEach(this.createSegment);
    this.labels.forEach(this.createLabel);
    this.element.appendChild(create("div", "wheel-of-fortune__arrow"));
  }

  createSegment = (label, index) => {
    const segment = create("div", "wheel-of-fortune__segment");
    const skew = this.degreeses - 90;

    segment.style.transform = `rotate(${
      this.degreeses * index + skew - this.degreeses / 2
    }deg) skewX(${skew}deg)`;

    this.container.appendChild(segment);
  };

  createLabel = (label, index) => {
    const labelNode = create("div", "wheel-of-fortune__label");
    const labelText = create("div", "wheel-of-fortune__label-text");

    labelText.appendChild(document.createTextNode(label));
    labelNode.appendChild(labelText);
    labelNode.style.transform = `rotate(${this.degreeses * index}deg)`;

    this.container.appendChild(labelNode);
  };

  spin = (index, round, body) => {
    function readCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
        return null;
      }

      let csrftoken = readCookie('csrftoken');
    fetch('http://127.0.0.1:8000/log/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(body),
    })
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));

    fetch('http://127.0.0.1:8000/round/1/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(body),
    })
    .then(response => response.text())
    .then(result => {
        if (result === '{"detail":"Not found."}') {
            fetch('http://127.0.0.1:8000/round/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(body),
            })
            .then(response => response.text())
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
        } else {
            console.log(result)
        }
    })
    .catch(error => console.log('error', error));

    if (this.isLock) return;

    this.isLock = true;

    const segmentDegreeses = this.degreeses * index - 90 - this.degreeses / 2;
    const randomDegreeses = (this.degreeses - 6) * Math.random() + 3;
    const animationRotate = 360 * this.animationSpins;
    const rotate = -segmentDegreeses - randomDegreeses - animationRotate;

    startAnimation(
      this.animationTime,
      (progress) => {
        this.container.style.transform = `rotate(${
          this.current + (rotate - this.current) * easeInOut(progress)
        }deg)`;
      },
      () => {
        this.current = rotate % 360;
        this.isLock = false;
      }
    );
  };
}

function startAnimation(duration, callback, finish) {
  let startAnimationTime = null;

  requestAnimationFrame(function measure(time) {
    if (!startAnimationTime) {
      startAnimationTime = time;
    }

    const progress = (time - startAnimationTime) / duration;

    callback(progress);

    if (progress < 1) {
      requestAnimationFrame(measure);
    } else {
      callback(1);
      finish();
    }
  });
}

function easeInOut(time) {
  return 0.5 * (1 - Math.cos(Math.PI * time));
}

function create(type, className) {
  const element = document.createElement(type);

  element.className = className;

  return element;
}
