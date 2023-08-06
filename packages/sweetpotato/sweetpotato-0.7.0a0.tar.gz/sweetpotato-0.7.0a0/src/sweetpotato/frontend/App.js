import React from "react";
import "react-native-gesture-handler";
import * as RootNavigation from "./src/components/RootNavigation";
import * as eva from "@eva-design/eva";
import { EvaIconsPack } from "@ui-kitten/eva-icons";
import { NavigationContainer } from "@react-navigation/native";
import { ApplicationProvider, IconRegistry } from "@ui-kitten/components";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Home } from "./src/screens/Home.js";

const Tab = createBottomTabNavigator();
export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    return (
      <NavigationContainer ref={RootNavigation}>
        <ApplicationProvider theme={{ ...eva.dark }}>
          <IconRegistry icons={EvaIconsPack} {...eva} />
          <Tab.Navigator>
            <Tab.Screen name={"Home"}>{() => <Home />}</Tab.Screen>
          </Tab.Navigator>
        </ApplicationProvider>
      </NavigationContainer>
    );
  }
}
