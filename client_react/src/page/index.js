//
//
import { lazy } from "react"

import Loadable from "../component/Loadable"

const UiTimer = Loadable(lazy(() => import('./ui-timer')))
const UiTimerApi = Loadable(lazy(() => import('./ui-timer-api')))

export { UiTimer, UiTimerApi }
