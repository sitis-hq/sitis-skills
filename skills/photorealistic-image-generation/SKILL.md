---
name: photorealistic-image-generation
description: Как собирать промпты для фотореалистичных, правдоподобных AI-изображений. Использовать всякий раз, когда нужно сгенерировать изображение, которое должно выглядеть как настоящий снимок (candid-фото, «случайный» кадр, документальная съёмка), а не как «нейросетевая картинка». Скилл отвечает за СБОРКУ промпта; выбор модели и выходного разрешения остаётся за рецептом/системой, которая его использует.
---

# Скилл: фотореалистичные AI-изображения

Назначение: помочь агенту собрать промпт так, чтобы изображение выглядело как реальный момент, пойманный фотографом, а не как стерильная «AI-картинка». Главный принцип реализма — **управляемое несовершенство**: правильная камера, уместный свет, живая текстура и мелкие дефекты.

> **Границы скилла.** Этот скилл — про ПРОМПТ: структуру, формулировки, камерный язык. Он НЕ выбирает модель и НЕ задаёт выходное разрешение — это решает рецепт/система, которая его подключает. Если инструкции рецепта расходятся с формулировками ниже по модели или размеру — приоритет у рецепта.

---

## 1. Модель и итерации

- **Модель выбирает рецепт/система, которая использует этот скилл.** Не подменяй модель по своей инициативе и не «перебирай» разные модели, если это прямо не предусмотрено задачей. Этот скилл о том, КАК написать промпт, а не ЧЕМ его сгенерировать.
- **Генерация дёшева — итерируй.** Реализм берётся не «правильной моделью», а промптом и перебором: прогоняй один и тот же промпт несколькими генерациями (разные seed'ы / повторы) в рамках выбранной моделью и отбирай лучший кадр. Качество кадра не объясняется одной магической настройкой.
- **Разные модели сильны в разном** — это правда, но ЧЕМ генерировать, здесь не решается. Когда задача всё же допускает выбор — сравнивай по результату, а не по репутации модели.
- **Текст на изображении** (таймкод, надписи): модели по-разному справляются с читаемым текстом. Если текст на кадре критичен — убедись, что выбранная рецептом модель его тянет, либо наноси текст пост-обработкой, а не промптом.

---

## 2. Метод CTLT — основа сборки промпта

Собирать промпт из четырёх частей **строго в порядке Camera → Tone → Lighting → Texture**. По одному предложению на часть; четыре предложения и есть промпт. Камера идёт первой, потому что способ съёмки задаёт весь характер кадра.

| Часть | Что задавать |
| :---- | :---- |
| **Camera** | Фотостиль + объектив (если полезно) + точка съёмки + кадрирование. |
| **Tone** | Настроение, атмосфера, эмоциональная энергия; затем — кто в кадре, что делает, где. |
| **Lighting** | Источник + направление + качество света + эффект на субъекте и фоне. |
| **Texture** | Материалы + видимые детали поверхностей + взаимодействие с движением/средой + зерно/шум (если уместно). |

**Приём тона «кадр, который не должны были видеть».** Для ощущения случайности задавать candid-настроение так, будто кто-то прошёл/проехал мимо и мельком снял сцену (passer-by). Это продаёт непостановочность.

**Эталонный пример (четыре предложения, затем склейка):**

```
Camera: Candid 35mm film photograph with a 12mm fisheye lens, slightly elevated side view, wide full-body framing, tilted horizon and slight motion blur.

Tone: Frantic, absurd and darkly comic, like an unexpected chase caught by a passerby. A skeleton wearing a dress made of raw meat sprints down a Los Angeles street at night, with three dogs chasing close behind.

Lighting: Harsh direct on-camera flash lights the skeleton and nearby dogs, casting hard shadows across the asphalt while the parked cars and street behind them fall into darkness.

Details: Matte ivory bones, glossy marbled meat with visible fat and uneven edges flapping with each stride, coarse dog fur, rough asphalt and visible film grain.
```

Разумные настройки для такого кадра: модель — ту, что задаёт рецепт; 16:9; разрешение — максимальное доступное у модели (понижать фактический размер только если этого прямо требует замысел кадра, см. раздел 5).

**Для сложных сцен** держать в голове CTLT, но выстраивать мысль так:
> overall look → subjects → decor → finish (общий вид → субъекты → окружение → финальная отделка).

---

## 3. Упрощённый шаблон: Scene → Camera → Details

Для простых промптов — три части, собираются склейкой по порядку. Работает даже для сюрреалистичных сцен.

| Часть | О чём думать |
| :---- | :---- |
| **Scene** | Кто / делает что / где? |
| **Camera** | Фотостиль / кадр / точка съёмки / объектив? |
| **Details** | Свет / текстура / несовершенства? |

**Пример:**

```
A skeleton in a meat dress running for its life down an LA street, three dogs chasing behind it. Candid 35mm film photo, low side view, 12mm fisheye. Harsh flash, visible film grain, crooked framing and a little motion blur.
```

---

## 4. Сборка промпта через LLM

Не обязательно формулировать всё вручную — «сырую» идею можно отдать LLM, которая соберёт её по структуре. Если есть лист персонажа / референсы — прикрепить и использовать метки `@image1`, `@image2`.

> **Про механизм референсов.** Инлайновые метки `@image1`/`@image2` — это условность для ЛЛМ-сборки промпта. Фактический способ передачи референсов зависит от системы: многие пайплайны принимают УПОРЯДОЧЕННЫЙ список изображений (напр. поле `image_urls`), а не инлайновые теги, и порядок/роль референсов там задаёт рецепт. Используй механизм хоста; если рецепт уже описал контракт референсов (кто первый, кто последний, что каждый задаёт) — следуй ему, а теги ниже держи как концептуальные.

**Служебный промпт для LLM:**

```
Turn my idea into an image-generation prompt that feels like a real moment caught by a photographer.

Follow this order:
1. Scene: subject, action and setting.
2. Camera: photographic style, shot and viewpoint. Add a suitable lens if useful.
3. Details: lighting and two or three visible qualities that support realism.
Preserve my idea. Add only what helps the image; don't invent extra subjects, props or elaborate backstories.
Make the camera choices coherent. Use grain, flash, motion blur or imperfect framing only when they suit the scene. Avoid generic claims like "masterpiece" or "8K." Don't add reference-image tags unless I supplied reference images. If I supplied references, preserve their actual @image1, @image2 labels and state what each reference contributes.
Return the ready-to-paste prompt, followed by a Scene / Camera / Details breakdown.
My idea: [PASTE YOUR IDEA]
```

Правила чистоты промпта (заложены в служебный промпт, применять всегда):
- Сохранять исходную идею; добавлять только то, что помогает изображению. Не выдумывать лишних субъектов, реквизит и предысторию.
- Выбор камеры должен быть согласованным.
- Зерно, вспышку, смаз, несовершенное кадрирование использовать **только когда они уместны для сцены**.
- Избегать штампов вроде «masterpiece», «8K».
- Теги референсов (`@image1`, …) добавлять только при наличии реальных референсов; указывать вклад каждого.

---

## 5. Слова, задающие стиль

Одна и та же идея при разном описании съёмки даёт разную визуальную идентичность. **Фразу о камере ставить первой.**

Готовый кадр можно **перефотографировать** в другом стиле, передав его как референс:

```
Rephotograph the scene and seated pose in @Image 2 as a harsh disposable-camera direct-flash snapshot. Use @Image 1 as the authoritative design of [SUBJECT].
```

**Низкофидельный ВИД — рабочий приём, но не ценой реального разрешения.** Ощущение реальности усиливают видимые артефакты: зерно, прямая вспышка, лёгкая компрессия, «снято на дешёвый телефон» — **несовершенное выглядит реальнее**. Важно, КАК этого добиваться: описывай низкофидельный ВИД **словами в промпте** (`visible film grain`, `mild compression artifacts`, `harsh on-camera flash`, `phone-camera noise in the shadows`), а не реальным понижением разрешения вывода. Снижать фактический размер/качество файла имеет смысл только там, где это допускает конечное использование; если задача требует высокого разрешения (печать обложки, последующий апскейл, анимация в видео) — **оставляй максимальное разрешение**, а «дешёвый» характер создавай исключительно формулировками.

---

## 6. Семь камерных стилей (готовые заготовки)

Выбирать **один** стиль за раз; **не смешивать несовместимые инструкции по камере**. Фразы — это направления, а не точные настройки: после генерации проверять, действительно ли изменились точка съёмки, кадрирование, текстура, смаз. Ниже вместо `[сцена]` подставлять свой субъект/действие/место.

### 6.1. Close skate-camera
```
Camera: Candid film photography shot close to the subject from knee height with a 12mm fisheye lens, wide framing, curved edges and a crooked horizon.
Tone: Raw, spontaneous and slightly absurd. [сцена]
Lighting: Harsh direct on-camera flash lights the subject and nearby ground, casting hard shadows behind it. Cool ambient light glows nearby while the background stays dark.
Texture: Visible fabric, foam, creased denim, scuffed shoes, rough pavement and noticeable film grain.
```

### 6.2. Phone snapshot (9:16)
```
Camera: Quick vertical phone snapshot taken at eye level while walking past, slightly tilted and loosely framed, with a little movement blur from the photographer's motion.
Tone: Casual, fleeting and unposed. [сцена]
Lighting: Available fluorescent light spills onto one side of the subject. Weak ambient lighting leaves uneven illumination and noisy shadows.
Texture: Visible fabric and foam, folds in cotton, creased denim and phone-camera noise in the darker areas.
```

### 6.3. Intimate documentary
```
Camera: Close handheld documentary photograph on 35mm film with a 35mm lens, taken at the subject's eye level, with waist-up framing and a slightly uneven crop.
Tone: Quiet, observational and unguarded. [сцена]
Lighting: Uneven light from one side falls across the subject, fading into soft shadow on the other side. The background remains dim but visible.
Texture: Visible fabric seams and foam, folds around the elbows, small grease marks and fine film grain.
```

### 6.4. Motion-blurred photo dump
```
Camera: A badly shaken handheld phone snapshot with strong diagonal camera-shake blur across the whole image, doubled edges and smeared shapes. The subject remains recognizable, with blur affecting both subject and background.
Tone: Chaotic, accidental and slightly absurd. [сцена]
Lighting: Available light illuminates the scene. Bright areas smear into diagonal streaks in the same direction as the camera shake.
Texture: Fabric, foam and denim read as soft blocks of texture, with coarse digital noise in the shadows and surfaces smeared by the camera movement.
```

### 6.5. Low curbside
```
Camera: Candid photograph shot from curb level with a 24mm wide-angle lens, full-body framing, feet close to the camera, the subject farther back and ground filling the foreground.
Tone: Mundane, unposed and quietly comic. [сцена]
Lighting: Cool light spills across the figure and ground. Weak ambient light catches the foreground, with deeper shadows below.
Texture: Visible fabric and foam, denim bunching at the knees, scuffed shoes and coarse ground close to the lens.
```

### 6.6. Disposable camera look
```
Camera: Found footage flash photograph. Shot at night on a cheap digital point-and-shoot camera, with everything mostly in focus, a quick unplanned composition and an imperfect crop.
Tone: Candid, mundane and slightly absurd. [сцена]
Lighting: Harsh built-in flash lights the subject from the front, casting a hard shadow behind it and clipping the brightest highlights. The background glows faintly.
Texture: Visible fabric and foam, creased denim, slightly crunchy digital detail, mild compression artifacts and noisy shadows.
```

### 6.7. Concealed observation
```
Camera: Telephoto photograph taken from inside a parked car, with compressed perspective and slightly soft focus. A blurred window edge and dashboard partially obscure the foreground.
Tone: Quiet, distant and unposed, the subject unaware of the camera. [сцена]
Lighting: Available light illuminates the subject across the street. The car interior stays dark, with weak ambient light falling unevenly.
Texture: Fabric and foam, creased denim, rough surfaces and visible grain, with faint reflections on the window glass.
```

---

## 7. Идея и уровни контраста

Собрать изображение — лёгкая часть; труднее придумать идею. Рабочий рычаг — **контраст между ожидаемым и неожиданным**: кадр должен вызывать реакцию «что это вообще такое?». Это и делает контент заметным и виральным.

Шкала контраста (на абстрактном примере персонажа):
- **Level 0 — нет контраста:** субъект там, где и ожидается (робот на заводе).
- **Level 1 — неожиданная ситуация:** тот же субъект в неожиданном месте (робот у зарядной станции).
- **Level 2 — неожиданная стилизация:** добавить характер/атрибутику (тот же робот «обвешан бриллиантами», с дерзкой подачей).
- **Level 3 — добавить чувство:** эмоциональный поворот (тот же робот, выключенный, в поле цветов — вызывает сочувствие).

Поднимать уровень осознанно под задачу: заметность — выше уровни, спокойная сцена — ниже.

---

## 8. Переиспользуемый стиль через .md-файл

Понравившийся визуальный стиль фиксировать в `.md`-файле и переиспользовать.

1. Отдать LLM понравившееся изображение вместе с промптом, который его породил, и попросить:
   ```
   Can you take the camera style based on this prompt that gave me this image and turn it into a reusable MD file?
   ```
2. Затем загружать этот `.md` в LLM с новой идеей — стиль переносится на новый сюжет. Работает, даже если непонятно, как именно получился удачный кадр.

**Структура такого файла:** описание основного стиля камеры, разделы Lens & Framing / Lighting / Exposure & Texture / Photographic Character, готовые к вставке версии (полная и короткая), перечень «что держать постоянным / что можно менять».

**Пример готового стилевого блока (короткая версия):**
```
12mm fisheye, extremely close low-angle night photo, near-ground viewpoint, strong barrel distortion, exaggerated foreground perspective, slightly crooked skate-photo framing, hard direct on-camera flash, bright flash-frozen subject against a dark ambient background, sharp specular highlights, deep shadows, dense blacks, visible 35mm film grain, raw DIY street-editorial feel.
```

**Полная версия:**
```
Camera: extremely close low-angle night photograph, shot from near ground level with a 12mm fisheye lens, strong barrel distortion, exaggerated foreground perspective, slightly crooked horizon, loose imperfect skate-photo framing. Hard direct on-camera flash dominates the exposure, creating bright crisp highlights on the subject, sharp local contrast and rapid falloff into a dark ambient background. Flash-frozen foreground, dim practical light in the environment, deep shadows, dense blacks, reflective surfaces catching sharp white speculars, visible 35mm-style film grain, raw late-night street-documentary texture, no polished studio softness, no HDR look.
```

Для серии в одном стиле держать постоянными: объектив и дистанцию камеры, точку съёмки, характер вспышки/света, тональную обработку и зерно. Свободно менять: субъект, позу/действие, одежду, локацию, реквизит, фон.

---

## 9. Чек-лист (пройти перед финальной генерацией)

- Модель и выходное разрешение — те, что задаёт рецепт/система (скилл их не меняет).
- При возможности сравнить несколько генераций (seed'ов / повторов) ОДНОЙ выбранной модели и отобрать лучшую.
- Камера описана первой; выбор объектива/света/текстуры согласован.
- Один камерный стиль, без несовместимых инструкций.
- Заложены уместные несовершенства (зерно, вспышка, смаз, кривой кадр, компрессия) — **как ВИД через формулировки**, не через реальное понижение разрешения; там, где они оправданы.
- Нет штампов («masterpiece», «8K») и лишних выдуманных субъектов/предысторий.
- Референсы передаются механизмом хоста (упорядоченный список / контракт рецепта); инлайновые теги — только при наличии реальных референсов.
- Есть контраст (ожидаемое vs неожиданное) под нужный уровень заметности.
- После генерации проверено: действительно ли изменились точка съёмки, кадрирование, текстура, смаз.
- Удачный стиль по возможности зафиксирован в `.md` для повторного использования.
